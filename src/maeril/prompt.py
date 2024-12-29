import re
import subprocess
from pathlib import Path


def replace_codefile(match):
    filepath_str = match.group(1).strip()
    filepath = Path(filepath_str)
    file_content = filepath.read_text()
    lines = file_content.splitlines()

    content_with_line_numbers = ""
    for line_number, line in enumerate(lines, start=1):
        content_with_line_numbers += f"{line_number:3}: {line}\n"

    # Extract the file extension for setting markdown hint
    md_hint = filepath.suffix.lower().lstrip(".") if filepath.suffix else 'text'

    formatted_code_block = (
        f"## {filepath}\n"
        f"\n"
        f"(With line numbers as a guide)\n"
        f"```{md_hint}\n"
        f"{content_with_line_numbers}"
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
    command_pattern = re.compile(r'\[command:\s*(.+?)\]')
    codefile_pattern = re.compile(r'\[codefile:\s*(.+?)\]')
    comment_pattern = re.compile(r'<!--.*-->')

    input_md = Path(input_path).read_text()
    input_md = input_md.rstrip()  # Remove trailing whitespace and newlines

    output_lines = []
    for line in input_md.splitlines():
        if comment_pattern.search(line):
            continue  # Skip lines containing comments
        line = command_pattern.sub(replace_command, line)
        line = codefile_pattern.sub(replace_codefile, line)
        output_lines.append(line)

    converted_md_content = ""
    for line in output_lines:
        converted_md_content += line + "\n"

    # Ensure the content ends with exactly one newline
    converted_md_content = converted_md_content.rstrip('\n') + '\n'

    output_path = "output.md"
    Path(output_path).write_text(converted_md_content)
    print(f"Converted {input_path} to {output_path}")
