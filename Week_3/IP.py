'''Defining the import'''

def is_prime(n):
    ip = False
    if n == 2:
        ip = True
    try:
        for i in range(2,int((n/2)+1)):
            if not n % i == 0:
                ip = True
            else:
                ip = False
                break
    except:
        ip = False
    return ip
# print(is_prime(100))