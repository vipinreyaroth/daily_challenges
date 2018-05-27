import collections

phoneBook = collections.defaultdict(str)


def search_phone_book(names):
    for name in names:
        print('{}={}'.format(name, phoneBook.get(name, 'Not found')) if phoneBook.get(name) else 'Not found')


def main():
    n = int(input().strip())
    names = list()

    for i in range(n):
        name, number = input().rstrip().split()
        phoneBook[name] = number

    while True:
        try:
            name = input().strip()
        except EOFError:
            break
        names.append(name)

    search_phone_book(names)


if __name__ == '__main__':
    main()