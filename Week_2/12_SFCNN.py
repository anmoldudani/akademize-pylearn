'''Sum of First Cubes of N Natural Numbers'''

def sums(n):
    sum = 0
    for i in range(n):
        sum += (i ** 3)
    return sum

n = 100
print(f'Sum of cubes of numbers till {n} is {sums(n)}')

'''
Output:
Sum of cubes of numbers till 100 is 24502500
'''