from main import read_and_list_input, item_is_not_digit, count_items, pairs_finder


# input parsing tests
def test_reading_input_blank_strings():
    input_list = read_and_list_input('input_blank_and_strings.txt')
    assert input_list == [4, 8, 9, 0, 12, 1, 4, 2, 12, 12, 4, 4, 12, 0]


def test_reading_input_decimal():
    input_list = read_and_list_input('input_decimal.txt')
    assert input_list == [9, 5.5, 6.5, 3, 5, 5, 5, 6, 8, 3, 7, 1, 1, 11, 12, 12]


# digit detection tests
def test_item_is_not_digit_1(item='03'):
    item_detected = item_is_not_digit(item)
    assert item_detected == 3


def test_item_is_not_digit2(item='[5.7'):
    item_detected = item_is_not_digit(item)
    assert isinstance(item_detected, float)


def test_item_is_not_digit3(item=' .'):
    item_detected = item_is_not_digit(item)
    assert item_detected == 'NaN'


# counting items tests
def test_counting_values_basic():
    input_list = read_and_list_input('input_basic.txt')
    counted_items = count_items(input_list)
    assert counted_items == {4: 4, 8: 2, 9: 1, 0: 2, 12: 4, 1: 1, 2: 1, 11: 1}


# pair finder test
def test_pair_finder_input_long():
    input_list = read_and_list_input('input_long.txt')
    counted_items = count_items(input_list)
    pairs = pairs_finder(counted_items)
    assert pairs == [[4, 8], [4, 8], [4, 8], [4, 8], [4, 8], [12, 0], [3, 9],
                     [3, 9], [3, 9], [5, 7], [1, 11], [5.5, 6.5], [7.5, 4.5]]
