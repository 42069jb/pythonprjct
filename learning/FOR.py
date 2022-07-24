n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(i,n):
        print(k,end="")
    for p in range(i,n):
        print(p+5,end="")
    print()