#!/usr/bin/env python3.11
number = input("Enter a number:")

def fizzbuzz(num):
      if num % 3 == 0 and num % 5 == 0:
            return "fizzbuzz"
      elif num % 3 == 0:
            return "fizz"
      elif num % 5 == 0:
            return "buzz"
      else:
            return num
for item in range(1,int(number)+1):
      print(fizzbuzz(item))