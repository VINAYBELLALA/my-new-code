def Fibonacci(n):
    if n==1 or n==0:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
Fibonacci(4)