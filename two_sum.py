"""Given an array of integers nums (list_input) and an integer target, return indices of the two numbers such that they
add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


def two_sum(list_input, target_value):
    output = list()
    for num in list_input:
        if (target_value - num) in list_input[list_input.index(num) + 1:]:
            output.append(list_input.index(num))
            list_input[list_input.index(num)] = '#'
            output.append(list_input.index(target_value - num))
    return output


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))
