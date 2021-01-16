'''Find Factorial of N'''

def fact(n):
    mul = 1
    for i in range(1, n+1):
        mul = mul * i
    return mul

n = 5
print(f'Factoial of {n} is {fact(n)}')

'''
Output:
Factoial of 5 is 120
'''