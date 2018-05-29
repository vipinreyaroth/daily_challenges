from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'date amount')


class Account:
    def __init__(self, owner, start_balance=0):
        self.owner = owner.title()
        self.start_balance = start_balance
        self._transactions = []

    # Using property for computed attributes
    @property
    def balance(self):
        tt = sum(t.amount for t in self._transactions)
        return self._start_balance + tt

    # Second use case is encapsulation
    @property
    def start_balance(self):
        return self._start_balance

    @start_balance.setter
    def start_balance(self, balance):
        if not isinstance(balance, int):
            raise TypeError('Balance needs to be an integer')

        if balance < 0:
            raise ValueError('Balance amount cannot be negative')
        self._start_balance = balance

    @start_balance.deleter
    def start_balance(self):
        raise AttributeError('The attribute start_balance')

    def _add_transaction(self, amount):
        if not isinstance(amount, int):
            raise TypeError('Amount needs to be integer')

        t = Transaction(date=datetime.now(), amount=amount)
        self._transactions.append(t)

    def __iadd__(self, amount):
        'Magic method to do account += amount. This is like operator overloading in other languages'
        self._add_transaction(amount)
        return self

    def __isub__(self, amount):
        'Magic method to do account -= amount. This is like operator overloading in other languages'
        self._add_transaction(-amount)
        return self

    def __len__(self):
        'Magic method to return the number of transactions'
        return len(self._transactions)

    def __str__(self):
        'This function helps to report or format a } object'
        tt = ['{} - {}'.format(t.date.strftime('%m/%d/%Y %H:%M:%S'), t.amount) for t in self._transactions]
        string = ['Account of {}'.format(self.owner),
                  'has a staring balance of {}'.format(self.start_balance),
                  'Transactions:',
                  '\n'.join(tt) or None,
                  'End balance: {}'.format(self.balance)]
        return '\n\n'.join(string)
