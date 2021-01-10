'''Simple Interest Calculator'''

P = float(input("Please enter the intial amount: "))
R = float(input("Please enter the rate per year (In decimal format): "))
T = float(input("Please enter the time it is invested (In years): "))

I = P * R * T

print(f"Your simple interest is {I}")

'''
Output:
Please enter the intial amount: 200000
Please enter the rate per year (In decimal format): 0.3
Please enter the time it is invested (In years): 3
Your simple interest is 180000.0
'''