#largest element brute ----->o(nlogn)
a=[3,4,2,1,2,3,9]
a.sort()
print(a)
print(a[-1])  

#largest element optimal ----->o(n)
a=[3,4,2,1,2,3,9]
largest=max(a)
print(largest)
