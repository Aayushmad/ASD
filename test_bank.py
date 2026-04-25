from bank import BankAccount

def test_deposit():
    acc = BankAccount("Aayush", 100)
    assert acc.deposit(50) == 150

def test_withdraw():
    acc = BankAccount("Aayush", 100)
    assert acc.withdraw(40) == 60

def test_insufficient_funds():
    acc = BankAccount("Aayush", 100)
    assert acc.withdraw(200) == "Insufficient funds"

def test_invalid_deposit():
    acc = BankAccount("Aayush", 100)
    assert acc.deposit(-10) == "Invalid amount"

def test_check_balance():
    acc = BankAccount("Aayush", 100)
    assert acc.check_balance() == 100