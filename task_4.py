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


snowball(7, 2)   


def snowman(n):
    pass
