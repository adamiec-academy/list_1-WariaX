def envelope(n): 
    for cheat1 in range(0, (2*n+1)):
        for cheat2 in range(0, (2*n+1)):
            if (cheat1 == 0 or cheat1 == (2*n+1) - 1
                or cheat2 == 0 or cheat2 == (2*n+1) - 1
                or cheat1 == cheat2 or cheat1 == (2*n+1) - 1 - cheat2):        
                print( "*", end="")
 
            else:
                print( " ",end="")
        print("")
envelope(10)
