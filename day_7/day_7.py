import os
import sys

TOTAL_DISC_SPACE = 70000000
FREE_DISC_SPACE_NEEDED = 30000000
DIRECTORY_TOTAL_MAX_SIZE = 100_000


def day_7(part_1: bool):
    all_directories = get_all_directories()

    sum_of_max_size_directories = 0
    for directory_id in all_directories:
        directory = all_directories[directory_id]
        sub_directories = [item for item in all_directories.keys() if item.startswith(directory_id)]
        for sub_id in sub_directories:
            if sub_id != directory_id:
                directory.total_sub_directories_size += all_directories[sub_id].file_sizes
        if directory.total_sub_directories_size <= DIRECTORY_TOTAL_MAX_SIZE:
            sum_of_max_size_directories += directory.total_sub_directories_size

    if part_1:
        return sum_of_max_size_directories
    else:
        free_space = TOTAL_DISC_SPACE - all_directories["root"].get_total_directory_size()

        min_viable_directory_size = TOTAL_DISC_SPACE
        for directory in all_directories.values():
            total_directory_size = directory.get_total_directory_size()
            if total_directory_size + free_space >= FREE_DISC_SPACE_NEEDED and total_directory_size < min_viable_directory_size:
                min_viable_directory_size = total_directory_size

        return min_viable_directory_size


def get_all_directories():
    with open(os.path.join(sys.path[0], 'day_7/input.txt')) as commands:
        top_directory = Directory(
            parent_id="",
            name="root",
        )
        all_directories = {top_directory.id: top_directory}
        extract_directories(all_directories, commands, top_directory)
    return all_directories


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
    total_sub_directories_size = 0

    def __init__(self, parent_id, name, directory_ids=None, file_sizes=0):
        if directory_ids is None:
            directory_ids = []
        self.id = get_id(parent_id, name)
        self.parent_id = parent_id
        self.name = name
        self.directory_ids = directory_ids
        self.file_sizes = file_sizes

    def get_total_directory_size(self):
        return self.total_sub_directories_size + self.file_sizes
