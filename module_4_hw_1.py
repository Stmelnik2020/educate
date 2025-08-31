from pathlib import Path

path_to_file = Path('salary.txt')


def total_salary(path: Path) -> tuple:
    """
    a function that parses a file and returns the total and average salary of all employees
    """
    employers_count = 0
    total_salary_sum = 0
    try:
        # open the file in read mode
        with open(path) as file:
            # start a loop to process the strings one by one
            for line in file:
                # increase the value of the variable "total_salary_sum" with each new string
                total_salary_sum += float(line.strip().split(',')[1])
                # increase the value of the variable "employers_count" with each new string
                employers_count += 1
        # find the average value by dividing the "total_salary_sum" by the "employers_count"
        average_salary = total_salary_sum / employers_count
        # return a tuple with two values: ("total_salary_sum", "average_salary")
        return (total_salary_sum, average_salary)
    # exception block
    except FileNotFoundError:
        return "File not found!"
    except IOError:
        return "Error while reading file!"
    except IndexError or ZeroDivisionError:
        return "Wrong data format in file"


print(total_salary(path_to_file))
