"""Print Lines."""


def print_line(n):
    """Print line with n characters."""
    for i in range(1,n+1):
        str1 = (' ' * (n-i)) + ('*' * (i))
        print(str1)

n = 10
print_line(n)

'''
Output:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
'''