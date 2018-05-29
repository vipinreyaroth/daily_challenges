import pytest
from account import Account

account = Account('vipin', 100)


def test_wrong_balance_type():
    with pytest.raises(TypeError):
        Account('vipin', 'spam')

    with pytest.raises(ValueError):
        Account('vipin', -100)


def test_deleter():
    with pytest.raises(AttributeError):
        del account.start_balance


def test_type_check_iadd_isub():
    acc = Account('barry', 100)
    with pytest.raises(TypeError):
        acc += 'test'

    with pytest.raises(TypeError):
        acc += 'case'


def test_balance():
    acc = Account('tom', 300)
    assert acc.start_balance == 300
    acc += 100
    assert acc.balance == 400
    acc -= 200
    assert acc.balance == 200
    assert len(acc) == 2


if __name__ == '__main__':
    pytest.main()
