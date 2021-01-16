'''Sum of First N Natural Numbers'''

def sums(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

n = 100
print(f'Sum of numbers till {n} is {sums(n)}')

'''
Output:
Sum of numbers till 100 is 4950
'''