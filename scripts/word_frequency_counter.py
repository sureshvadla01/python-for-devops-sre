def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example
print(word_frequency("hello world hello"))
# Output: {'hello': 2, 'world': 1}
