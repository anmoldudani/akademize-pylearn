"""Arithmetic Operators.
Action	                        Common Symbol
---------------------------------------------
Addition	                        +
Subtraction	                        -
Multiplication	                    *
Division	                        /
Modulus (associated with integers)	%
"""

a = 2020
b = 2021

print(str(a) + " + " + str(b) + " = " + str(a+b))
# 15 + 2 = 17

print(f"{a} - {b} = {a-b}")

print("{} * {} = {}".format(a, b, a*b))

print("{x} / {y} = {div}".format(y=b, x=a, div=a/b))

print(f"{a} // {b} = {a//b}")

print(f"{a} % {b} = {a%b}")

'''
Output:
2020 + 2021 = 4041
2020 - 2021 = -1
2020 * 2021 = 4082420
2020 / 2021 = 0.9995051954477981
2020 // 2021 = 0
2020 % 2021 = 2020
'''