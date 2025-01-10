from sort.quick_sort import quick_sort_in_place, quick_sort_new_arrays


def test_quick_sort_in_place__empty():
    assert quick_sort_in_place([]) == []


def test_quick_sort_in_place__one_element():
    assert quick_sort_in_place([9]) == [9]


def test_quick_sort_in_place__two_elements():
    assert quick_sort_in_place([2, 9]) == [2, 9]


def test_quick_sort_in_place__three_elements():
    assert quick_sort_in_place([5, 1, 9]) == [1, 5, 9]


def test_quick_sort_in_place__five_elemements():
    assert quick_sort_in_place([5, 4, 1, 2, 9]) == [1, 2, 4, 5, 9]


def test_quick_sort_in_place__sorted():
    assert quick_sort_in_place([1, 2, 4, 5, 9]) == [1, 2, 4, 5, 9]


def test_quick_sort_new_arrays_new_arrays__empty():
    assert quick_sort_new_arrays([]) == []


def test_quick_sort_new_arrays_new_arrays__one_element():
    assert quick_sort_new_arrays([9]) == [9]


def test_quick_sort_new_arrays_new_arrays__two_elements():
    assert quick_sort_new_arrays([2, 9]) == [2, 9]


def test_quick_sort_new_arrays_new_arrays__three_elements():
    assert quick_sort_new_arrays([5, 1, 9]) == [1, 5, 9]


def test_quick_sort_new_arrays__simple_five_elemements():
    assert quick_sort_new_arrays([5, 4, 1, 2, 9]) == [1, 2, 4, 5, 9]


def test_quick_sort_new_arrays__sorted():
    assert quick_sort_new_arrays([1, 2, 4, 5, 9]) == [1, 2, 4, 5, 9]
