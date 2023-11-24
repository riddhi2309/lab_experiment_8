x = int(input("enter the number:-"))
list = []
for i in range(x):
    n=float(input("enter the number"))
    list.append(n)
y = None
for i in list:
    if y==None or i>y :
        y = i
print(y)
