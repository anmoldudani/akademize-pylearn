  
"""Print a multiplication table."""


def print_table(n):
    """Print nth table."""
    print(f"Table {n}\n----------")
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")

n = 11
print_table(n)

'''
Output:
Table 11
----------
11 * 1 = 11
11 * 2 = 22
11 * 3 = 33
11 * 4 = 44
11 * 5 = 55
11 * 6 = 66
11 * 7 = 77
11 * 8 = 88
11 * 9 = 99
11 * 10 = 110
'''