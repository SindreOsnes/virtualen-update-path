import os

def update_path_in_bat_file(filepath: str, path_addition: str) -> None:
    """Add a line for path updates to the specified file

    :param str filepath: The path to the file to update
    :param str path_addition: The folder to add to the path variable

    :raises FileNotFoundError: if the path getting added is not valid 
    """

    if not os.path.isdir(path_addition):
        raise FileNotFoundError("Path does not exist")

    with open(filepath, 'a', encoding='utf8') as f:
        f.write(f'\nset "PATH={path_addition};%PATH%"\n')
