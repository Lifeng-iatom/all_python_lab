#!/usr/bin/env python3.11
length = 5
pic = '*'

for i in range(length):
      for j in range(length-i):
            print(' ',end='')
      print(pic)

      pic +='**'

length -=1
space = 1
astNum = length*2 -1 
pic='*'*astNum

for i in range(length):
      print(' '+space*' ' + pic)
      space+=1
      astNum -=2
      pic='*'*astNum
      
      
