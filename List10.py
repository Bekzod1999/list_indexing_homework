# def main(list_num):
#     """
#     A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
#     Args:
#         list_num (list): parameter
#     Returns:
#         int: return answer
#     """
#     largestNumber = 0
#     i = 0
#     k = list_num[0]
#     while i < len(list_num):
        
#         if list_num[i] > k:
#             k = list_num[i]
#         i += 1

#     return k
# x = main([-5, 0, -1, -4, -30])
# print(x)



def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    largestNumber = 0
            
    if list_num[0] > list_num[-1]:
        return list_num[0]
    else:
        return list_num[-1]
x = main([12, 2, 5, 2, 7, 9, 100])
print(x)