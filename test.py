from main import read_and_list_input, count_items


def test_reading_input_blank_strings():
    input_list = read_and_list_input('input_blank_and_strings.txt')
    assert input_list == [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 12, 0]


def test_reading_input_decimal():
    input_list = read_and_list_input('input_decimal.txt')
    assert input_list == [9, 5.5, 6.5, 3, 5, 5, 5, 6, 8, 3, 7, 1, 1, 11, 12, 12]


def test_counting_values_basic():
    input_list = read_and_list_input('input_basic.txt')
    counted_items = count_items(input_list)
    assert counted_items == {4: 4, 8: 2, 9: 1, 0: 2, 12: 4, 1: 1, 2: 1, 11: 1}
