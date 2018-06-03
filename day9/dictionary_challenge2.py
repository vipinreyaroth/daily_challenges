"""
Statement
Given the text: the first line contains the number of lines, then given the lines of words. Print the word in the text that occurs most often. If there are many such words, print the one that is less in the alphabetical order.
"""

n = int(input())
words_dict = {}

for _ in range(n):
    words = input().split()
    for word in words:
        words_dict[word] = words_dict.get(word, 0) + 1

max_count = max(words_dict.values())
words = [k for k, v in words_dict.items() if v == max_count]
print(min(words))
