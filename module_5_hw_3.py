import sys
from pathlib import Path


# checking the number of input arguments from the command line
if len(sys.argv) > 2:
    sys_arguments, path_argument, mode = sys.argv
    file_path = Path(path_argument).absolute()
    target_level = mode
elif len(sys.argv) < 3:
    sys_arguments, path_argument = sys.argv
    file_path = Path(path_argument).absolute()


def parse_log_line(line: str) -> dict:
    """
    takes a line from the log as an input
    parameter and returns a dictionary
    with parsed components:
    date, time, level, message
    """
    # create an empty dictionary
    parsed_line = {}
    # store values ​​by keys in a dictionary
    parsed_line["date"] = line.split()[0]
    parsed_line["time"] = line.split()[1]
    parsed_line["level"] = line.split()[2]
    parsed_line["message"] = ' '.join(line.split()[3:])
    return parsed_line


def load_logs(file_path: str) -> list:
    """
    opens a file, reads each line,
    and applies the parse_log_line function to it,
    saving the results to a list
    """
    # create an empty list
    logs_list = []
    # read lines from the log file sequentially
    with open(file_path) as file:
        for line in file.readlines():
            # add strings to the list
            logs_list.append(parse_log_line(line))
    return logs_list


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    gets all log entries
    for a specific logging level
    """
    # create an empty list
    targeted_messages = []
    # check the line for consistency with the required log level
    for lvl in logs:
        if lvl["level"] == level.upper():
            targeted_messages.append(lvl)
    return targeted_messages


def count_logs_by_level(logs: list) -> dict:
    """
    goes through all records and counts
    the number of records for each logging level
    """
    # create an empty dictionary
    level_counter = {}
    # count the number of logs by level
    for line in logs:
        if line.get('level') not in level_counter:
            level_counter[f'{line.get('level')}'] = 1
        else:
            level_counter[f'{line.get('level')}'] += 1
    return level_counter


def dictionary_unpacker(list: list) -> str:
    """
    function that transforms dictionaries
    into a string with the required formatting
    """
    # unpack the values ​​from the dictionary into a readable format
    for element in list:
        print(f'{element.get("date")} {element.get("time")} - {element.get("level")} {element.get("message")}')


def display_log_counts(counts: dict) -> str:
    """
    function that formats and outputs
    calculation results in a readable form.
    """

    # create a variable that contains strings of the required format
    message = f'Рівень логування | Кількість\n\
-----------------|----------\n\
INFO             | {counts.get("INFO")}\n\
DEBUG            | {counts.get("DEBUG")}\n\
ERROR            | {counts.get("ERROR")}\n\
WARNING          | {counts.get("WARNING")}\n'
    result = f'{message}'
    return result


def main():
    # excepting errors block
    try:
        # if 3 arguments are received from the command line
        if len(sys.argv) > 2:
            # displays log counter by level
            print(display_log_counts(count_logs_by_level(load_logs(file_path))))
            # a line is added for informativeness
            print(f'Деталі логів для рівня "{target_level.upper()}":')
            # display a list of logs at the specified level
            dictionary_unpacker(filter_logs_by_level(
                load_logs(file_path), target_level))
        # if the user did not specify a log level in the arguments
        elif len(sys.argv) < 3:
            # displays log counter by level
            print(display_log_counts(count_logs_by_level(load_logs(file_path))))
    # error handling
    except FileNotFoundError:
        print("Невірний шлях до файлу або такого файлу не існує!")


if __name__ == "__main__":
    main()
