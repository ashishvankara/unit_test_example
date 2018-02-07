def test_sum_list():
    from do_stuff import sum_list
    s = sum_list([1, 2, 3])
    assert s == 6

def test_min_max():
    from do_stuff import min_max_list
    (a, b) = min_max_list([5, 4, 1, 2])
    assert a == 2
