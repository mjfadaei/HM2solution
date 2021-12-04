import datetime
n=int(input("Pleas Enter n: "))
def Fibonacci(n): 
    
    if n==0: 
        return 0
     
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2)
    
a= datetime.datetime.now()
print(a)
print(Fibonacci(n))
b = datetime.datetime.now()
print(b)
c=b-a
print("Time for fibo:" )
print(int(c.total_seconds()*1000))
