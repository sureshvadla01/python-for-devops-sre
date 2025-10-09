def first_unique_char(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

# Example
print(first_unique_char("aabbcdde"))
# Output: "c"