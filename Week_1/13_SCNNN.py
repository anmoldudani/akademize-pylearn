'''Sum of Cubes of N Natural Numbers'''

n = 10
sum = 0
for i in range(n):
    sum = pow(i,3) + sum

print(f"Sum of first {n} Natural numbers is {sum}")

'''
Output:
Sum of first 10 Natural numbers is 285
'''