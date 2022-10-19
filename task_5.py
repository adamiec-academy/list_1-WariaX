def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial



def report():
    
    for i in range(1, 101): 
        a = len(str(factorial(i)))
        print(f"{i : >3}! is {a: >3} digits long")
        


report() 
