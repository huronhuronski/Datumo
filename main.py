from collections import Counter
from os import getcwd
from os.path import join
from re import sub
from sys import exit
from typing import List, Dict, Union


def read_local_input(input_file_name: str) -> str:
    """Returns string that can be later parsed and converted to list.

    Function reads first line of indicated text file.
    File has to be located in same directory as this module.
    """
    with open(input_file_name, 'r') as input_file:
        input_string = input_file.readline()
    return input_string


def list_input(input_string: str) -> List[Union[int, float]]:
    """Returns list of integers (and/or floats) derived from input file.

    This function uses help of item_is_not_digit() function in cases
    when item cannot be converted to integer right away.
    """
    input_list = []
    for item in input_string.split(','):
        item = item.strip()
        try:
            input_list.append(int(item))
        except ValueError:
            number_check = item_is_not_digit(item)
            if not isinstance(number_check, str):
                input_list.append(number_check)
    return input_list


def item_is_not_digit(item: str) -> Union[int, float, str]:
    """Evaluates disrupted input.

    It tries to pull out a numerical value from input: integer or float (if input contains ".").
    If numerical value cannot be pulled out, function returns NaN (not a number).
    """
    regex = '[^0-9.]'
    try:
        return int(sub(regex, '', item))
    except ValueError:
        try:
            return float(sub(regex, '', item))
        except ValueError:
            return 'NaN'


def count_items(input_list: List[Union[int, float]]) -> Dict[Union[int, float], int]:
    """Returns dictionary with numbers from input list in keys and how many times they appeared in values."""
    counter = Counter(input_list)
    return dict(counter)


def pairs_finder(counter_dict: Dict[Union[int, float], int]) -> List:
    """Returns list of numbers that add up to 12.

    It firstly calculates a complementary number for one that is being evaluated.
    Then it starts for loop that checks how many times number under evaluation can form a pair.
    Exception for number 6, it needs to have at least value 2 to form a pair (not like other numbers).
    If complementary number is not present in dict then inner for loop gets terminated.
    """
    pairs = []
    for key, value in counter_dict.items():
        complementary = 12 - key
        for i in range(value):
            if key == 6 and value < 2:
                break
            if complementary in counter_dict.keys() and counter_dict[complementary] != 0:
                pairs.append([key, complementary])
                counter_dict[key] -= 1
                counter_dict[complementary] -= 1
            else:
                break
    return pairs


def write_output(pairs: List):
    """Function writes pairs of numbers into output.txt file in same directory as this module."""
    output_file = open('output.txt', 'w')
    for pair in pairs:
        output_file.write(str(pair) + ' ')
    output_file.close()


def main():
    """Function that executes this program in terminal."""
    while True:
        input_file = input('If you want to quit, write "q"\n'
                           'Otherwise, indicate the input .txt file you want to process: ')
        if not input_file.lower().strip() == 'q':
            try:
                input_string = read_local_input(input_file)
                input_list = list_input(input_string)
            except FileNotFoundError:
                print("No such file in the directory: " + getcwd())
                continue
            counter_dict = count_items(input_list)
            pairs = pairs_finder(counter_dict)
            write_output(pairs)
            print(join(getcwd(), input_file))
            exit()
        else:
            print("Bye!")
            exit()


if __name__ == '__main__':
    main()
