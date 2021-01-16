"""Else if ladder, Find age group."""


def print_age_group(age):
    """Print Age group for a given age."""
    if age < 5:
        print(f"Age = {age}, Age Group = Infant")
    elif age < 12:
        print(f"Age = {age}, Age Group = Toddler")
    elif age < 20:
        print(f"Age = {age}, Age Group = Teen")
    elif age < 60:
        print(f"Age = {age}, Age Group = Adult")
    else:
        print(f"Age = {age}, Age Group = Sr. Citizen")


# Start executing...
print_age_group(3)
print_age_group(7)
print_age_group(14)
print_age_group(45)
print_age_group(70)

'''
Output:
Age = 3, Age Group = Infant
Age = 7, Age Group = Toddler
Age = 14, Age Group = Teen
Age = 45, Age Group = Adult
Age = 70, Age Group = Sr. Citizen
'''