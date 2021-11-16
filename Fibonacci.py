Seq = int(input("enter sequence: "))
if(Seq == 1):
    Fib = 1
    print(Fib)
else:
    Fib = 0
    for n in range(Seq,0,-1):
        Fib += n
print(f'Fibonacci of {Seq} is {Fib}')