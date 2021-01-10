'''Compound Interest Calculator'''

P = float(input("Please enter the intial amount: "))
R = float(input("Please enter the rate per year (In decimal format): "))
T = float(input("Please enter the time it is invested (In years): "))
N = T = float(input("Please enter the periods elapsed (In years): "))

A = P * pow((1 + R/T), N * T)

print(f"Your compound interest is {A}")

'''
Output:
Please enter the intial amount: 200000
Please enter the rate per year (In decimal format): 0.3
Please enter the time it is invested (In years): 3
Please enter the periods elapsed (In years): 6
Your compound interest is 1158363.2271943737
'''