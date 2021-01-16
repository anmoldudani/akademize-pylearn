"""Function example."""


def print_age_group(age):
    """Print Age group for a given age."""
    if age < 5:
        print(f"Age = {age}, Age Group = Infant")
    else:
        if age < 12:
            print(f"Age = {age}, Age Group = Toddler")


# Start executing...
print_age_group(3)
print_age_group(7)

'''
Output:
Age = 3, Age Group = Infant
Age = 7, Age Group = Toddler
'''