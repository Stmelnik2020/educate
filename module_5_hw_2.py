from typing import Generator, Callable
import re

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


def generator_numbers(text: str) -> Generator:
    """
    takes a string as an argument and 
    returns a generator that iterates 
    over all real numbers in the text
    """
    # create an empty list to store all found numbers
    founded_numbs = []
    # a loop that reads text and then separates it with spaces
    for numb in text.split():
        # create a variable called "values" that checks strings for numbers
        values = re.findall(r"\d+\.\d+", numb)
        # if the values ​​contain a number, add it to the "founded_numbs" list
        if values:
            # define the generator
            yield values
            founded_numbs.extend(values)
    return founded_numbs


def sum_profit(text: str, func: Callable):
    """
    uses the generator_numbers generator
    to calculate the total sum of numbers
    in the input string
    """
    # create a variable to increment with new values ​​from the generator
    total_sum = 0
    # create a loop using a generator to get all the numbers contained in the text strings
    for numb in func(text):
        # increment the variable "total_sum" by the value from the generator
        total_sum += float(numb[0])
    return total_sum


total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
