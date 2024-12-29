import re
import subprocess
from pathlib import Path


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

    md_content = ""
    for line in input_md.splitlines():
        if comment_pattern.search(line):
            continue  # Skip lines containing comments
        line = command_pattern.sub(replace_command, line)
        line = codefile_pattern.sub(replace_codefile, line)
        md_content += f"{line}\n"

    # Ensure the content ends with exactly one newline
    md_content = md_content.rstrip('\n') + '\n'

    output_filename = f"{input_path.stem}.generated{input_path.suffix}"
    output_path = input_path.with_name(output_filename)

    Path(output_path).write_text(md_content)
    print(f"Converted {input_path} to {output_path}")
