#!/usr/bin/env python3.11
length = 7
space = 0
num = 2*length -1
logo=num*'*'
for i in range(length):
      print(space*' '+logo)
      space+=1
      num-=2
      logo=num*'*'

