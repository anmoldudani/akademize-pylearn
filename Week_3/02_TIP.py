'''Try is Prime'''
from IP import is_prime

def print_prime(n):
    bul = is_prime(n)
    if bul:
        print(f'{n} is prime.')
    else:
        print(f"{n} isn't prime.")

print_prime(200)

'''
Output:
200 isn't prime.
'''