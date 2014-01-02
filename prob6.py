def sumsqr(x,y):
    count = 0
    for i in range(x,y):
        count += i**2
    return count

def sqrsum(x,y):
    count = 0
    for i in range(x,y):
        count += i
    return count**2

difference = sqrsum(1,101) - sumsqr(1,101)

print difference


