r = int(input("enter the number of rows:-"))
c = int(input("enter the number of columns:-"))
m1=[]
m2=[]
sum_m=[]
for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("Enter the number:-"))
        l.append(v)
    m1.append(l)

for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("Enter the number:-"))
        l.append(v)
    m2.append(l)

for i in range(r):
    l=[]
    for j in range(c):
        sum = m1[i][j]+m2[i][j]
        l.append(sum)
    sum_m.append(l)

print("matrix 1\n")
for i in m1:
    print(i)

print("matrix 2\n")
for i in m2:
    print(i)
    
print("sum of matrix 1 and matrix 2\n")
for i in sum_m:
    print(i)
