import os
import sys

DIRECTORY_TOTAL_MAX_SIZE = 100_000


def day_7_part_1():
    with open(os.path.join(sys.path[0], 'day_7/input.txt')) as commands:
        top_directory = Directory(
            parent_id="",
            name="root",
        )
        all_directories = {top_directory.id: top_directory}
        extract_directories(all_directories, commands, top_directory)

        sum_of_max_size_directories = 0
        for directory in all_directories:
            sub_directories_sizes = all_directories[directory].file_sizes
            sub_directories = [item for item in all_directories.keys() if item.startswith(directory)]
            for sub_id in sub_directories:
                if sub_id != directory:
                    sub_directories_sizes += all_directories[sub_id].file_sizes
            if sub_directories_sizes <= DIRECTORY_TOTAL_MAX_SIZE:
                sum_of_max_size_directories += sub_directories_sizes

    return sum_of_max_size_directories


def extract_directories(all_directories, commands, top_directory):
    current_directory = top_directory
    for index, command in enumerate(commands.readlines()):
        command = command.strip()
        if command.startswith("$"):
            current_directory = execute_command(all_directories, command, current_directory, top_directory)
        elif command.startswith("dir"):
            handle_directory(all_directories, command, current_directory)
        else:
            current_directory.file_sizes += int(command.split(" ")[0])


def handle_directory(all_directories, command, current_directory):
    directory_name = command.split(" ")[1]
    new_directory = Directory(
        parent_id=current_directory.id,
        name=directory_name,
    )
    new_directory_id = new_directory.id
    if new_directory_id not in all_directories:
        all_directories[new_directory_id] = new_directory
        all_directories[current_directory.id].directory_ids.append(new_directory_id)
        current_directory.directory_ids.append(new_directory_id)


def execute_command(all_directories, command, current_directory, top_directory):
    command = command[2:len(command)]
    parent_id = current_directory.parent_id
    if command == "cd ..":
        current_directory = all_directories[parent_id] if parent_id in all_directories else top_directory
    elif command == "cd /":
        current_directory = top_directory
    elif command.startswith("cd"):
        directory_name = command.split(" ")[1]
        target_id = get_id(current_directory.id, directory_name)
        if target_id in all_directories:
            current_directory = all_directories[target_id]
    return current_directory


def get_id(parent_id, name):
    return parent_id + "/" + name if parent_id != "" else name


class Directory:
    def __init__(self, parent_id, name, directory_ids=None, file_sizes=0):
        if directory_ids is None:
            directory_ids = []
        self.id = get_id(parent_id, name)
        self.parent_id = parent_id
        self.name = name
        self.directory_ids = directory_ids
        self.file_sizes = file_sizes
