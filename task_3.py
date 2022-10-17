def envelope(n): 
    for cheat1 in range(0, n):
        for cheat2 in range(0, n):
            if (cheat1 == 0 or cheat1 == n - 1
                or cheat2 == 0 or cheat2 == n - 1
                or cheat1 == cheat2 or cheat1 == n - 1 - cheat2):        
                print( "*", end="")
 
            else:
                print( " ",end="")
        print("")
envelope(10)
