#!/usr/bin/env python3.11
length = 7

logo = '*'
for i in range(length):
      for j in range(length-i-1):
            print(' ',end='')
      print(logo)
      logo += '**'