a=[0,1,5,2,4]
a.sort()
print(a)
m=False
for i in range(len(a)-1):
   if(a[i+1]-a[i]!=1):
       print(a[i]+1)
       m=True
       break
if not m:
    print(a[-1]+1)