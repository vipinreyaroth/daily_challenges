"""
This exercise is to explain the use of properties. This is based on Pybytes article by Bob Belderos.
"""
from account import Account


def main():
    acc = Account('Vipin', 200)
    acc += 400
    acc -= 100
    print(acc)


if __name__ == '__main__':
    main()
