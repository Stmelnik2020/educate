from pathlib import Path

path_to_file = Path('cats_info.txt')


def get_cats_info(path: Path) -> list[{dict}]:
    '''
    a function that reads a file and returns a list of dictionaries with information about each cat
    '''
    cats_list_info = []  # create an empty list that will be filled with dictionaries
    try:
        # open the file in read mode
        with open(path) as file:
            # start a loop that will process each string in the file
            for line in file:
                # clean and split each string into three variables respectively
                id, name, age = line.strip().split(",")
                # create a dictionary with three key-value pairs
                dict = {"id": f"{id}", "name": f"{name}", "age": f"{age}"}
                cats_list_info.append(dict)  # add dictionary to the list
        return cats_list_info
    except FileNotFoundError:
        return "File not found!"
    except IOError:
        return "Error while reading file!"
    except ValueError or IndexError:
        return "Wrong values in file!"


print(get_cats_info(path_to_file))
