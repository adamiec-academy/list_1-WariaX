def chess_board(n, k): 

    for fortheemperor in range(n):

        for deus in range(k): 
            for vult in range (n):        
                print((" " * k ) + ("#" * k ), end="")
            print()     
            
        for satan in range(k): 
            for vult in range (n):        
                print(("#" * k ) + (" " * k ), end="")
            print()   

chess_board(4, 2)
