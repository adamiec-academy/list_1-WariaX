def cross(n):
    for i in range(1 , (3 * n)+1):
        if i <= n:
            print((n * " ") + (n * "X") + (n * " "))      
    
        elif i > (n + 1) and i <= (2 * n):            
            print ((n * 3) * "X")

        elif i > (2 * n):
            print((n * " ") + (n * "X") + (n * " "))

cross(4)
