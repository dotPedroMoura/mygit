from pathlib import Path


def write_tree (directory = '.'):
    for entry in Path(directory).iterdir():
        if is_ignored(entry):
            continue
        if entry.is_file() and not entry.is_symlink():
            print(entry)
        elif entry.is_dir() and not entry.is_symlink():
            write_tree(entry)

def is_ignored(path):
    if path in Path('.mygitignore').read_text().splitlines():
        return True