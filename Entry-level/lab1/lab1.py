#!/usr/bin/env python3.11
fahr = float(input("with the temp you want to convert in F:"))
cel = round((fahr-32)*5/9,2)
print(f"{fahr}F is {cel}C")