def is_subset(list1, list2):
    return set(list1).issubset(set(list2))

# Example
print(is_subset([1, 2, 3], [1, 2, 3, 4, 5]))
# Output: True