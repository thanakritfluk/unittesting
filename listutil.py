def count_unique(list):
    """Count the number of distinct elements in a list.

    The list can contain any kind of elements, including duplicates and nulls in any order.

    (In PyDoc there are different formats for parameters and returns. Use what you prefer.)

    :param list:  list of elements to find distinct elements of
    :return: the number of distinct elements in list

    Examples:
    >>> count_unique(['a','b','b','b','a','c','c'])
    3
    >>> count_unique(['a','a','a','a'])
    1
    >>> count_unique([ ])
    0
    """
    if len(list) == 0:
        return 0
    list.sort()
    check = list[0]
    count = 1
    for i in list:
        if i != check:
            count += 1
            check = i
    return count


def binary_search(list, element):
    """
         Find the element from sorted list with Binary Search.
        :params list: sorted list of elements to search
                element: element to search
        :return: index of element, -1 if not found.
        >>> binary_search([34, 44, 102, 2], 1)
        -1
        >>> binary_search([5, 6, 7, 8, 9], 8)
        3
        >>> binary_search([10, 11, 12, 17, 25,50,75], 25)
        4
        >>> binary_search([0, 0, 0, 0, 0], 0)
        2
        >>> binary_search([2, 6, 12, 20, 25, 34, 68], 34)
        5

    """
    if list is None:
        raise TypeError("Search element must not be none")
    first = 0
    last = len(list) - 1
    while first <= last:
        mid = (first + last) // 2
        if list[mid] == element:
            return mid
        if list[mid] < element:
            first = mid + 1
        else:
            last = mid - 1
    return -1
