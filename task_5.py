def factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial



def report(n):
    
    for i in range(1, n+1): 
        a = len(str(factorial(i)))
        print(f"{i : >4}! is {a: >3} digits long")
        


report(100) 
