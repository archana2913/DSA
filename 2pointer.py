a=list(map(int,input().split()))
i=0
for j in range(len(a)):
    if(a[i]!=a[j]):
        a[i+1]=a[j]
        i+=1
print(*a)
print(*a[:i+1])
