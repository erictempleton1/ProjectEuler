def multiply(x,y):
    for num1 in range(x,y):
        for num2 in range(x,y):
            multip = num1 * num2
            if int(str(multip)[::-1]) == int(str(multip)) and multip > 900000:
                return multip
                
            

print multiply(100,1000)