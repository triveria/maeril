import re
import subprocess
from pathlib import Path
import tiktoken
import pyperclip


def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Text has been copied to clipboard")


def print_token_usage(text, model="o1-mini"):
    match model:
        case "gpt-4o":
            cost_per_token = 2.50 / 1_000_000
            context_window = 128000
            name = "GPT-4o"
            encoding_name = "o200k_base"
        case "o1":
            cost_per_token = 15 / 1_000_000
            context_window = 128000
            name = "o1"
            encoding_name = "o200k_base"
        case "o1-mini":
            cost_per_token = 3 / 1_000_000
            context_window = 128000
            name = "o1-mini"
            encoding_name = "o200k_base"
        case _:
            raise ValueError(f"Unsupported model: {model}")

    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)

    num_tokens = len(tokens)
    cost = num_tokens * cost_per_token

    print(f"Number of tokens: {num_tokens}")
    print(f"Your prompt is roughly {num_tokens / 450:.1f} book pages long and fills out {num_tokens / context_window * 100:.0f}% of {name}'s {context_window/1000:.0f}k token context window.")
    print(f"Cost: ${cost:.6f} (Remember: 1 minute of your time costs 1€)")


def replace_codefile(match):
    filepath_str = match.group(1).strip()
    filepath = Path(filepath_str)
    file_content = filepath.read_text()
    lines = file_content.splitlines()

    content = ""
    for line in lines:
        content += f"{line}\n"

    # Extract the file extension for setting markdown hint
    md_hint = filepath.suffix.lower().lstrip(".") if filepath.suffix else 'text'

    formatted_code_block = (
        f"## {filepath}\n"
        f"\n"
        f"```{md_hint}\n"
        f"{content}"
        f"```\n"
    )

    return formatted_code_block


def replace_command(match):
    command = match.group(1).strip()
    command_output = subprocess.check_output(command, shell=True, text=True).rstrip()
    formatted_command_block = (
        f"## output of `{command}`\n"
        f"\n"
        f"```sh\n"
        f"{command_output}\n"
        "```"
    )
    return formatted_command_block


def main(input_path):
    input_path = Path(input_path)
    command_pattern = re.compile(r'\[command:\s*(.+?)\]')
    codefile_pattern = re.compile(r'\[codefile:\s*(.+?)\]')
    comment_pattern = re.compile(r'<!--.*-->')

    input_md = input_path.read_text()
    input_md = input_md.rstrip()  # Remove trailing whitespace and newlines

    generated_prompt = ""
    for line in input_md.splitlines():
        if comment_pattern.search(line):
            continue  # Skip lines containing comments
        line = command_pattern.sub(replace_command, line)
        line = codefile_pattern.sub(replace_codefile, line)
        generated_prompt += f"{line}\n"

    # Ensure the content ends with exactly one newline
    generated_prompt = generated_prompt.rstrip('\n') + '\n'

    output_filename = f"{input_path.stem}.generated{input_path.suffix}"
    output_path = input_path.with_name(output_filename)

    Path(output_path).write_text(generated_prompt)
    print(f"Converted {input_path} to {output_path}")

    copy_to_clipboard(generated_prompt)
    print_token_usage(generated_prompt)
