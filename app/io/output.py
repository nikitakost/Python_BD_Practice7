def print_to_console(text):
    """
    Prints given txt to console
    :param: text to be written
    :return: printed text
    """
    print(text)

def write_to_file(path, text):
    """
    Writes txt to file using built-i features
    :param: Path to the file
    :param: text
    :return: txt to file
    """
    with open(path, "w", encoding="utf-8") as file:
        file.write(text)