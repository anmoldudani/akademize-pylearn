'''Sum of First Squares of N Natural Numbers'''

def sums(n):
    sum = 0
    for i in range(n):
        sum += (i ** 2)
    return sum

n = 100
print(f'Sum of squares of numbers till {n} is {sums(n)}')

'''
Output:
Sum of squares of numbers till 100 is 328350
'''