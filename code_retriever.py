import argparse
import os
import subprocess
import pyperclip

# Mapping of common programming languages to their file extensions
LANGUAGE_EXTENSIONS = {
    'python': ['.py'],
    'javascript': ['.js'],
    'java': ['.java'],
    'cpp': ['.cpp', '.cxx', '.h', '.hpp'],
    'csharp': ['.cs'],
    'ruby': ['.rb'],
    'php': ['.php'],
    'swift': ['.swift'],
    'go': ['.go'],
    'typescript': ['.ts']
}

def clone_repo(repo_url, target_dir):
    """Clones the repository to a local directory."""
    subprocess.run(["git", "clone", repo_url, target_dir], check=True)

def extract_code(base_path, exclude_files, include_extensions, recursive):
    """Extracts code from files in the given base_path, with specified options."""
    code_lines = []
    for root, dirs, files in os.walk(base_path):
        if not recursive and root != base_path:
            continue
        for file in files:
            if file not in exclude_files and any(file.endswith(ext) for ext in include_extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        code_lines.extend(f.readlines())
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
    return code_lines

def parseargs():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Extracts code and comments from a directory or GitHub repository, with options for exclusions, language filtering, and recursion control.")
    parser.add_argument("repo_or_directory_path", type=str, help="Directory path or GitHub repository URL")
    parser.add_argument("target_subdirectory", type=str, help="Target subdirectory within the path or repository")
    parser.add_argument("--exclude-files", type=str, default="README.md,LICENSE", help="Comma-separated list of files to exclude")
    parser.add_argument("--languages", nargs='+', help="Programming languages to filter by", choices=list(LANGUAGE_EXTENSIONS.keys()))
    parser.add_argument("--recursive", action='store_true', help="Include files in all subdirectories recursively")
    args = parser.parse_args()

    # Split comma-separated strings into lists and accumulate extensions for specified languages
    args.exclude_files = args.exclude_files.split(',')
    include_extensions = []
    if args.languages:
        for lang in args.languages:
            include_extensions.extend(LANGUAGE_EXTENSIONS[lang])
    else:
        # If no languages are specified, default to include all extensions
        include_extensions = [ext for extensions in LANGUAGE_EXTENSIONS.values() for ext in extensions]

    args.include_extensions = list(set(include_extensions))  # Remove duplicates

    return args

def main():
    args = parseargs()

    repo_or_dir = args.repo_or_directory_path
    target_subdir = args.target_subdirectory
    exclude_files = args.exclude_files
    include_extensions = args.include_extensions
    recursive = args.recursive

    # Clone the repository if the source is a GitHub URL
    if repo_or_dir.startswith("https://github.com"):
        target_dir = "temp_repo"
        clone_repo(repo_or_dir, target_dir)
        base_path = os.path.join(target_dir, target_subdir)
    else:
        base_path = os.path.join(repo_or_dir, target_subdir)

    code_lines = extract_code(base_path, exclude_files, include_extensions, recursive)
    
    # Copy the extracted code to the clipboard
    pyperclip.copy(''.join(code_lines))
    print("Code and comments have been copied to clipboard.")
    
    # Cleanup cloned repository if applicable
    if repo_or_dir.startswith("https://github.com"):
        subprocess.run(["rm", "-rf", target_dir], check=True)

if __name__ == "__main__":
    main()
