"""Practice #60: BankAccount encapsulation (attempt 2)."""

class BankAccount:
    """Encapsulation: balance only changes through methods."""

    def __init__(self, owner):
        self.owner = owner
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount


if __name__ == "__main__":
    acct = BankAccount("me")
    for d in [67, 31, 176, 127]:
        acct.deposit(d)
    acct.withdraw(7)
    print(acct.owner, "has", acct.balance)
    assert acct.balance == 394
