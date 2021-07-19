# Python offers several ways to reverse a String. This is a classic thing
# that lots of people want to do. It's probably easy to look up this
# answer on Stack Overflow.
#
# This website of 30 Python Tips and Tricks also happens to point out
# several ways to reverse a string, and it's a good read!
#
# http://www.techbeamers.com/essential-python-tips-tricks-programmers/?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more#tip1


# text = "reverse_me"[::-1]
# print(text)

def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str

s = "reverse_me"
# print(s)
# print(reverse(s))


def reverse2(s):
  if len(s) == 0:
    return s
  else:
    return reverse2(s[1:]) + s[0]
print(reverse2(s))