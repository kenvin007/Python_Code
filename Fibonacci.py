Seq = int(input("enter sequence: "))
if(Seq == 1):
    Fib = 1
    print(Fib)
else:
    li = []
# 0,1,2,3,5,8,13
    curr = 1
    li.append(1)
    li.append(1)
    for i in range(0,Seq):
        val = li[i] + li[i+1]
        li.append(val)
        print(val, end=" ")
print()