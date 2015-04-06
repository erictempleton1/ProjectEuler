def collatz(n):
    count = 1
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count



start_num = 1
long_chain = 0
for x in range(1,1000000):
    leng = collatz(x)
    if leng > long_chain:
        start_num = x
        long_chain = leng

print start_num
print long_chain