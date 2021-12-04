def fibo(n):
    first = 1
    second = 1
    c = 1
    while c < n:
        T = first + second
        first = second
        second = T
        c = c + 1
    print(first)

n = int(input('enter number n: '))
fibo(n)
