def sum_list(number_list):
    """sum all the numbers in number_list
    """
    import numpy as np

    s = np.sum(number_list)

    return s


def min_max_list(number_list):
    """find the min/max of the list
    """
    import numpy as np

    d = np.array(number_list)
    mi = d.min()
    ma = d.max()

    return (mi, ma)
