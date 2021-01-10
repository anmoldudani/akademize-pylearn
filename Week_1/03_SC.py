"""String Concatenation."""

name = "Jaeck"
location = "Fairy Land"

print(name + " lives in " + location)

age = 180

# The below line Throws an Error: TypeError:
# can only concatenate str (not "int") to str
# print(name + " is an " + age + " year oldman.")
print(name + " is an " + str(age) + " year old man.")

'''
Output:
Jaeck lives in Fairy Land
Jaeck is an 180 year old man.
'''