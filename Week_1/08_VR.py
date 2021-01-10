""" Voter's Report """
print("_______Voter's Report_________")

name = input("Please enter your Name here : ")

age = int(input("Please enter your Age here : "))

if age>18:
    print(name + " can vote in the election. \nPlease follow procedures to do so.")

else :
    print("I am sorry " + name + " Please wait till you are 18 Years old")

'''
Output:
_______Voter's Report_________
Please enter your Name here : Jaeck    
Please enter your Age here : 25
Jaeck can vote in the election.
Please follow procedures to do so.
'''