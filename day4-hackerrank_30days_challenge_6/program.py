"""
Objective
Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops.
Check out the Tutorial tab for learning materials and an instructional video!

Task
Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as
space-separated strings on a single line (see the Sample below for more detail).

Note:  is considered to be an even index.

Input Format

The first line contains an integer,  (the number of test cases).
Each line  of the  subsequent lines contain a String, .

Constraints

Output Format

For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.
"""
import sys
from collections import deque


def print_odd_and_even_characters(string):
    even_index_chars = []
    odd_index_chars = []

    for i, c in enumerate(string):
        if not i % 2:
            even_index_chars.append(c)
        if i % 2 > 0:
            odd_index_chars.append(c)

    print('{} {}'.format(''.join(even_index_chars), ''.join(odd_index_chars)))


def main():
    nlines = int(input())

    if nlines not in range(1, 11):
        sys.exit(0)

    i = 0
    lines = list()
    while i < nlines:
        i += 1
        string = input()
        if len(string) not in range(2, 10001):
            continue

        if string:
            lines.append(string)

    lines = deque(lines)
    while (lines):
        print_odd_and_even_characters(lines.popleft())


if __name__ == '__main__':
    main()
