import pandas as pd

def input_from_console():
    """
    Reads info input from console
    :return: user's input as a String
    """
    return input("Enter some text: ")

def read_file_builtin(path):
    """
    Reads text from a file using Python built-in func
    :param: Path to the file
    :return: file content as a string
    """
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

def read_file_pandas(path):
    """
    Reads data from a file using pandas library
    :param: Path to the file
    :return: file content as a data frame
    """
    return pd.read_csv(path)
