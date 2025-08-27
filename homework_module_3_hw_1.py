import random


def get_numbers_ticket(min_value: int, max_value: int, quantity: int) -> list:
    """
    The function generates the specified number of unique numbers 
    in the given range and returns a list of randomly selected, sorted numbers.
    If the parameters do not meet the given constraints, the function returns an empty list.
    """

    numbers_ticket = []  # create an empty list to then add the result of the loop to it

    if min_value < 1 or max_value > 1000 or quantity >= max_value or min_value > max_value or quantity < min_value:  # check the input parameters
        return numbers_ticket
    else:
        while len(numbers_ticket) < quantity:  # loop for generating random numbers
            # transform the list into a set to avoid duplicates of the generation result
            numbers_ticket = set(numbers_ticket)
            # add the result of generation to the set
            numbers_ticket.add(random.randrange(min_value, max_value))
        # transform the set into a list for sorting
        numbers_ticket = list(numbers_ticket)
        numbers_ticket.sort()
        return numbers_ticket


lottery_numbers = get_numbers_ticket(1, 1000, 1000)
print("Ваші лотерейні числа: ", lottery_numbers)
