"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be: 
  
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... 
  
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. 
"""

def fib():
    fib_result = []
    a, b = 1, 2
    while a < 4000000:
        fib_result.append(a)
        a, b = b, a+b
    return fib_result

even_fib = []
for nums in fib():
    if nums % 2 == 0:
        even_fib.append(nums)

print sum(even_fib)





       



        
  
  
# try making three functions for each level of the problem and printing all with sum 
