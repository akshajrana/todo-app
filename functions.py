def fetch_todo(filepath = "todos.txt"):
    """
    Returns the contents of the file
    """
    with open(filepath, "r") as x:
        contents = x.readlines()
    return contents

def write_todo(contents, filepath = "todos.txt"):
    """
    Writes the contents to the file
    """
    with open(filepath, "w") as x:
        x.writelines(contents)