def cross(n):
    for i in range(0 , (3 * n)):
        if i < n:
            print((n * " ") + (n * "*") + (n * " "))      
    
        elif i >= (n ) and i < (2 * n):            
            print ((n * 3) * "*")

        elif i >= (2 * n):
            print((n * " ") + (n * "*") + (n * " "))

cross(4)
