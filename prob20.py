def factorial(n):
    product = 1
    for nums in n:
        product *= (nums+1)
    return product

print factorial(range(100))

def sum_list(x):
    return sum([int(nums) for nums in str(x)])

print sum_list(factorial(range(100)))


# combined in one function
def factorial_sum(n):
    product = 1
    for nums in n:
        product *= (nums+1)
    return sum([int(num) for num in str(product)])

print factorial_sum(range(100))s
    