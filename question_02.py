a = list(map(int,input("enter the list:- ").split()))
b =[]
while a:
    min_val = min(a)
    b.append(min_val)
    a.remove(min_val)
print(b)

