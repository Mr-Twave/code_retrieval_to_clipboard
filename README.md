### README.md for code_retriever.py

# Code Extractor

A versatile Python script for extracting code from specified directories or GitHub repositories. It supports filtering by programming languages, excluding specific files, and controlling the depth of recursion into subdirectories.

## Features

- Extract code from local directories or clone GitHub repositories to work with.
- Filter files to include by specifying one or more programming languages.
- Exclude specific files by name.
- Control whether to recursively search subdirectories or only include the specified directory.

## Requirements

- Python 3
- `pyperclip` module for clipboard operations (`pip install pyperclip`)
- Git installed if cloning from GitHub repositories.

## Usage

### Basic Command

```bash
python code_extractor.py <path_or_url> <target_subdirectory> [options]
```

### Options

- `--exclude-files`: Comma-separated list of files to exclude. Default is "README.md,LICENSE".
- `--languages`: Space-separated list of programming languages to filter by (e.g., `python javascript`). Supported languages include python, javascript, java, cpp, csharp, ruby, php, swift, go, typescript.
- `--recursive`: Include this flag to search all subdirectories recursively.

### Examples

Extract Python files from a local directory, excluding `example.txt`:

```bash
python code_extractor.py /path/to/local/repo subdirectory --exclude-files "example.txt" --languages python --recursive
```

Extract Java and C++ files from a GitHub repository:

```bash
python code_extractor.py https://github.com/username/repo subdirectory --languages java cpp --recursive
```

## License

This project is open source and available under the [Apache 2.0 License].
