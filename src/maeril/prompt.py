import re
import subprocess
from pathlib import Path
import tiktoken
import clipman
import logging


def copy_to_clipboard(text):
    clipman.init()
    clipman.set(text)
    logging.info("Full prompt has been copied to clipboard")


def print_token_usage(text, model="gemini-2.5-pro"):
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
        case "o3-mini":
            cost_per_token = 1.10 / 1_000_000
            context_window = 200000
            name = "o3-mini"
            encoding_name = "o200k_base"
        case "claude-3.7-sonnet":
            cost_per_token = 3 / 1_000_000
            context_window = 200000
            name = "Claude 3.7 Sonnet"
            encoding_name = "cl100k_base"
        case "gemini-2.5-pro":
            cost_per_token = 1.25 / 1_000_000 * 1.05  # add 5% due to using openrouter.ai
            context_window = 1_000_000
            name = "Gemini 2.5 Pro"
            encoding_name = "o200k_base"  # not true, but close enough
        case _:
            raise ValueError(f"Unsupported model: {model}")

    encoding = tiktoken.get_encoding(encoding_name)
    tokens = encoding.encode(text)

    num_tokens = len(tokens)
    cost = num_tokens * cost_per_token

    logging.info(f"Number of tokens: {num_tokens}")
    logging.info(
        f"Your prompt is roughly {num_tokens / 450:.1f} book pages long and fills out "
        f"{num_tokens / context_window * 100:.0f}% of {name}'s "
        f"{context_window/1000:.0f}k token context window."
    )
    logging.info(f"Cost: ${cost:.6f} (Remember: 1 minute of your time costs 1€)")


def replace_codefile(match):
    filepath_str = match.group(2).strip()
    filepath = Path(filepath_str)
    file_content = filepath.read_text().rstrip()
    lines = file_content.splitlines()

    content = ""
    for (line_number, line) in enumerate(lines, start=1):
        # content += f"{line_number:3}: {line}\n"
        content += f"{line}\n"

    # Extract the file extension for setting markdown hint
    md_hint = filepath.suffix.lower().lstrip(".") if filepath.suffix else "text"

    # Open WebUI only uses syntax highlighting for `python`, not `py`
    if md_hint == "py":
        md_hint = "python"

    # Use quad backticks for markdown blocks
    if md_hint == "md":
        formatted_code_block = (
            f"### {filepath}\n"
            f"\n"
            f"````{md_hint}\n"
            f"{content}\n"
            f"````\n"
        )

    else:
        formatted_code_block = (
            f"### {filepath}\n"
            f"\n"
            f"```{md_hint}\n"
            f"{content}\n"
            f"```\n"
        )

    return formatted_code_block


def replace_command(match):
    """
    Executes a shell command from a regex match and returns its formatted output.

    If the command fails, it raises a RuntimeError containing the stderr to ensure
    the specific cause of failure is the final message in the stack trace.
    """
    command = match.group(2).strip()
    result = subprocess.run( command, shell=True, text=True, capture_output=True )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())

    command_output = result.stdout.rstrip()
    formatted_command_block = (
        f"output of `{command}`:\n"
        f"\n"
        f"```sh\n"
        f"{command_output}\n"
        "```"
    )
    return formatted_command_block


def main(input_path, cli_mode):
    input_path = Path(input_path)

    command_pattern = re.compile(r'(!{)(.+)(})')
    if cli_mode:
        codefile_pattern = None
    else:
        codefile_pattern = re.compile(r'^(@)(\S+)')

    comment_pattern = re.compile(r'<!--.*-->')
    input_md = input_path.read_text()
    input_md = input_md.rstrip() # Remove trailing whitespace and newlines

    generated_prompt = ""
    for line in input_md.splitlines():
        if comment_pattern.search(line):
            continue  # Skip lines containing comments

        line = command_pattern.sub(replace_command, line)

        if codefile_pattern: # Only execute substitution if the pattern is not None
            line = codefile_pattern.sub(replace_codefile, line)
        generated_prompt += f"{line}\n"

    # Ensure the content ends with exactly one newline
    generated_prompt = generated_prompt.rstrip("\n") + "\n"

    output_filename = f"{input_path.stem}.generated{input_path.suffix}"
    output_path = Path("/tmp") / output_filename

    output_path.write_text(generated_prompt)
    logging.info(f"Generated prompt saved to: {output_path.absolute()}")

    copy_to_clipboard(generated_prompt)
    print_token_usage(generated_prompt)
