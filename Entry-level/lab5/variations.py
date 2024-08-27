#!/usr/bin/env python3.11
new_string = input("Enter a meassage:")
print(f"this is a lowercase {new_string.lower()}")
print(f"this is a uppercase {new_string.upper()}")
print(f"this is a cap {new_string.capitalize()}")
print(f"this is a title {new_string.title()}")
words = new_string.split()
print(words)
new_words = sorted(words,reverse = False)
print(new_words[0])
new_words = sorted(words,reverse = True)
print(new_words[0])


