"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
mult_list = []
for x in range(1,11):
    for y in range(1,11):
        mult_list.append(x*y)

print mult_list
        