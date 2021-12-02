class BankAccount:

    def __init__(self, initial_balance=0):
        self._balance = initial_balance
        self._transactions = []
        self._transactions.append(0)
        # create the list of transactions
        
    def deposit(self, amount):
        # save +amount on the list of transactions
        self._balance += amount
        self._transactions.append(amount)
        
    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError('Not sufficient funds')
        # save -amount on the list of transactions
        self._balance -= amount
        self._transactions.append(-amount)

    @property
    def balance(self):
        return self._balance

    def __getitem__(self, index):
        return self._transactions[index]
        # Your Code Here

### Expected behaviour
acc = BankAccount(initial_balance=0)
assert acc.balance == 0  # 2nd requirement

print (acc[0])

# acc.balance = 0  # ==> AttributeError: can't set attribute
acc.deposit(2000)
acc.withdraw(500)
acc.deposit(1000)
assert acc.balance == 2500

# 4th requirement -- __getitem__
assert acc[1] == 2000
assert acc[2] == -500
assert acc[3] == 1000
# acc[3]  # ==> IndexError
for transaction in acc:
    print(transaction)
print("Transactions:", list(acc))