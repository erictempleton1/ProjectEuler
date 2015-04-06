def sum_tri(n): 
    return sum([n + 1 for n in range(n)]) 
  
print sum_tri(7) 
  
def list_tri(x,y): 
    tri_sum = [sum_tri(nums) for nums in range(x,y)] 
    return tri_sum 
  
print list_tri(1,11)

def factors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

print factors(sum_tri(7))


        
    
