import re
import subprocess
from pathlib import Path


def replace_codefile(match):
    filepath_str = match.group(1).strip()
    return generate_codefile_block(filepath_str)


def generate_codefile_block(filepath_str):
    filepath = Path(filepath_str)
    content = filepath.read_text()
    content_with_lines = '\n'.join(f"{i+1}: {line}" for i, line in enumerate(content.splitlines()))
    extension = filepath.suffix[1:] or 'text'
    return f"```{extension}\n## content of {filepath}, including line numbers.\n{content_with_lines}\n```"


def main(input_path):
    command_pattern = re.compile(r'\[command:\s*(.+?)\]')
    codefile_pattern = re.compile(r'\[codefile:\s*(.+?)\]')
    comment_pattern = re.compile(r'<!--.*-->')

    input_md = Path(input_path).read_text()

    output_lines = []
    for line in input_md.splitlines():
        if comment_pattern.search(line):
            continue  # Skip lines containing comments
        # Replace [command: ...]
        line = command_pattern.sub(
            lambda m: f"```sh\n## output of `{m.group(1).strip()}`\n{subprocess.check_output(m.group(1).strip(), shell=True, text=True).rstrip()}\n```",
            line
        )
        # Replace [codefile: ...]
        line = codefile_pattern.sub(
            replace_codefile,
            line
        )
        output_lines.append(line)

    converted_md = '\n'.join(output_lines)
    output_path = "output.md"
    Path(output_path).write_text(converted_md)
    print(f"Converted {input_path} to {output_path}")
