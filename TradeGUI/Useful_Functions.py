import os
from enum import Enum


class ListType(Enum):
    WatchList = 1
    DataList = 2
    TrainingList = 3


# Input comes from buttons, you give it a name, and a string it writes to an output file
def write_strings_to_file(output_file, input_string, list_type):
    words = input_string.split(" ")
    directory = os.getcwd() + "\AssetList\\" + retrieveList(list_type)
    if not os.path.exists(directory):
        os.makedirs(directory)
    output_file = os.path.join(directory, output_file)
    with open(output_file, "w") as f:
        f.write(list_type.name + "\n")
        for word in words:
            f.write(word + "\n")
    print(f"File {output_file} has been written to the {directory} directory.")

# This reads the strings from the list creation menu but might impement more functionality later
def read_strings_from_file(file_name, list_type):
    directoryString = retrieveList(list_type)
    directory = os.getcwd() + "\AssetList\\" + directoryString
    file_path = os.path.join(directory, file_name)
    with open(file_path, "r") as f:
        content = f.read()
    lines = content.split("\n")
    if list_type.name != lines[0]:
        return None
    else:
        return lines

#This might be totally useless might delete later
def retrieveList (list_type):
    switch_dict = {
        ListType.DataList: "DataList",
        ListType.WatchList: "WatchList",
        ListType.TrainingList: "TrainList"
    }
    return switch_dict.get(list_type, "Invalid list type")