import mistune
from pathlib import Path

def read_files() -> list:
    input_folder = Path("input")
    md_files = list(input_folder.glob("*.md"))
    results = []
    for file in md_files:
        content = file.read_text()
        results.append((file.stem, content))
    return results

def convert(content: str) -> str:
    return str(mistune.html(content))

def convert_files(file_list: list) -> None:
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)
    for filename, content in file_list:
        html = convert(content)
        (output_folder / f"{filename}.html").write_text(html)
        print(f"Converted {filename}.md -> {filename}.html")


def main():
    file_list = read_files()
    convert_files(file_list)

if __name__ == "__main__" :
    main()