import sys
from pathlib import Path
from colorama import Fore

input_path = Path(sys.argv[1])


def paint_tree(user_path: Path):
    """
    function that prints a directory tree to the console
    """
    try:
        # function for iterating through subfolders
        def iterator(path: Path, level=0):
            for item in path.iterdir():
                # block of conditions for checking on an object PATH (folder or file)
                if item.is_dir():
                    print(Fore.BLUE + ('    '*level) + item.name + '/')
                    iterator(item, level + 1)
                else:
                    print(Fore.GREEN + ('    '*level) + item.name)
        # print the name of the starting directory
        print(
            Fore.WHITE + f'The following objects were found in the directory:  {user_path.name}/')
        # call recursion to find all subfolders
        iterator(user_path)
    # error handling
    except NotADirectoryError as DirectoryError:
        print(
            Fore.RED + f"{DirectoryError}  !!!    Enter argument in format - <script name> absolute/path/to/directory")
    except FileNotFoundError as FileError:
        print(
            Fore.RED + f"{FileError} !!!    Enter argument in format - <script name> absolute/path/to/directory")
    except IndentationError as IndentError:
        print(
            Fore.RED + f"{IndentError} !!!    Enter argument in format - <script name> absolute/path/to/directory")


paint_tree(input_path)
