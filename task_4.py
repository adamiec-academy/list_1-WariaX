def snowman (n):    
    def snowball(n, k):
        promien = (n / 2) - 0.5
        for i in range(n):
            print(2 * k * " ", end="")
            for j in range(n):
                x = i - promien
                y = j - promien
                if x * x + y * y <= promien * promien + 1:
                    print('#', end='  ')
                    
                else:
                    print(' ', end='  ')
            
            print()

        promien2 = ((n+2) / 2) - 0.5
        for i in range(n+2):
            print(k * " ", end="")
            for j in range(n+2):
                x = i - promien2
                y = j - promien2
                if x * x + y * y <= promien2 * promien2 + 1:
                    print('#', end='  ')
                    
                else:
                    print(' ', end='  ')
            
            print()    


        promien3 = ((n+4) / 2) - 0.5
        for i in range(n+4):
            for j in range(n+4):
                x = i - promien3
                y = j - promien3
                if x * x + y * y <= promien3 * promien3 + 1:
                    print('#', end='  ')
                    
                else:
                    print(' ', end='  ')
            
            print() 


    snowball(n, n-4)
snowman (7)
