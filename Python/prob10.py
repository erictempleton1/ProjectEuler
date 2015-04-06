# prime number generator. slow for very large numbers
def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

prime_list = []
for a in range(2,2000000):
    if isprime(a):
        prime_list.append(a)


print sum(prime_list)