#!/usr/bin/env python3.11
# 1) Write a `split_name` function that takes a string and returns a dictionary with first_name and last_name
def split_name(name):
      s_name=name.split(maxsplit=1)
      name ={}
      name["first_name"]=s_name[0]
      name["last_name"]=s_name[-1]
      return name

split_name("Kevin Bacon")
assert split_name("Kevin Bacon") == {
    "first_name": "Kevin",
    "last_name": "Bacon",
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

# 2) Ensure that `split_name` can handle multi-word last names

assert split_name("Victor Von Doom") == {
    "first_name": "Victor",
    "last_name": "Von Doom",
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Doom')}"

# 3) Write an `is_palindrome` function to check if a string is a palindrome (reads the same from left-to-right and right-to-left)

def is_palindrome(message):
      return str(message) == str(message)[::-1]

is_palindrome('radar')
is_palindrome("stop")
is_palindrome(101)
is_palindrome(10)

assert is_palindrome("radar") == True, f"Expected True but got {is_palindrome('radar')}"
assert is_palindrome("stop") == False, f"Expected False but got {is_palindrome('stop')}"

# 4) Make `is_palindrome` work with numbers

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"

# 5) Write a `build_list` function that takes an item and a number to include in a list
def build_list(message,number=1):
      message_list = []
      for num in range(number):
            message_list.append(message)
      return message_list
build_list("Apple", 3) 
build_list("Orange")


assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"