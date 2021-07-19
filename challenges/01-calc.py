# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.


def add(num1, num2):
  return num1 + num2

def sub(num1, num2):
  return num1 - num2

def multi(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2

print("Select operation.")
print("add")
print("subtract")
print("multiply")
print("divide")

while True:
  choice = input('Enter Choice("add","subtract","multiply","divide"): ')

  if choice in ("add","subtract","multiply","divide"):
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
    if choice == "add":
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == "subtract":
      print(num1, "-", num2, "=", sub(num1, num2))
    elif choice == "multiply":
      print(num1, "*", num2, "=", multi(num1, num2))
    elif choice == "divide":
      print(num1, "/", num2, "=", div(num1, num2))
    break
  else:
    print("invalid")