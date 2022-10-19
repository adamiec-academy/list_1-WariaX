def snowball(n, k):
        promien = (n / 2) - 0.5
        for i in range(n):
            print(k * " ", end="")
            for j in range(n):
                x = i - promien
                y = j - promien
                if x * x + y * y <= promien * promien + 1:
                    print('#', end='')                    
                else:
                    print(' ', end='')
            print()         

def snowman(n):
    snowball(n, 2)
    snowball((n+2), 1)
    snowball((n+4), 0)

snowman(7)
