a= list(map(int, input("enter list:-").split()))

total=1
i=0

while i<len(a):
    A= a[i]
    total = total*A
    i+=1
print(total)