print("Welcome to Chase bank.")
print("Have a nice day!")


class Bankaccount:
  def __init__(self):
    self.balance = 0

  def deposit(self):
    amount = float(input("Enter Amount to be deposited: "))
    self.balance += amount
    print("\n Amount Deposited:", amount)

  def withdraw(self):
    amount = float(input("Enter Amount to be withdrawn: "))
    if self.balance >= amount:
      self.balance -= amount
      print("\n You withdrew: ", amount)
    else:
      print("insufficient funds")

  def display(self):
    print('\n Net Available Balance =', self.balance)


s = Bankaccount()
s.deposit()
s.withdraw()
s.display()