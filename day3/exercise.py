from collections import deque


def rotate_string(text, n):
    """One way to rotate strings"""
    return f'{text[n:]}{text[:n]}'


def main():
    # Option 1
    print(rotate_string('vipin', 2))
    print(rotate_string('vipin', -2))

    # Option 2
    d = deque('vipin')
    print(d)
    d.rotate(2)
    print(d)
    d.rotate(-2)
    print(d)


if __name__ == '__main__':
    main()
