# prime number generator. slow for very large numbers
def isprime(n):
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

# prime list
prime_list = []
for a in range(2,14):
    if isprime(a):
        prime_list.append(a)
print prime_list

# nth prime
primes = 0
n = 1
while primes < 10001:
    n += 1
    if isprime(n) == True:
        primes += 1
print n
