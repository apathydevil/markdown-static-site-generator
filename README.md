# markdown-static-site-generator

A simple conversion programme using the mistune library. Files in the `input` folder are converted to .html and sent to the `output` folder.

## Requirements
- Python 3.10 or above
- mistune (`pip install mistune`)

## How to use
1. Clone the repo and navigate to it:
```
git clone https://github.com/apathydevil/markdown-static-site-generator
cd markdown-static-site-generator
```
2. Drop your `.md` files into the `input` folder
3. Run the script:
```
python main.py
```
4. Find your converted files in the `output` folder

## Testing
A `test.md` file is included in the `input` folder to demonstrate the conversion. It covers headings, paragraphs, bold, italic, lists, links, code blocks and blockquotes.

## What I learned
My third project. I learned how to use a third party library, work with the pathlib module to navigate folders, and convert files from one format to another automatically.