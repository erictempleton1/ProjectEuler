""" 
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. 
  
What is the sum of the digits of the number 2^1000? 
  
"""
  
def power_sum(n): 
    return sum([int(nums) for nums in str(2**n)])
 
print power_sum(1000)