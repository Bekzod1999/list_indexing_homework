def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    largestNumber = 0
    i = 0
    k = 0
    while i < len(list_num):
        if list_num[i] > k:
            k = list_num[i]
        i += 1

    return k
x = main([5, 9, 1, 2])
print(x)