r = int(input("enter the number of rows:-"))
c = int(input("enter the number of columns:-"))
m1=[]

for i in range(r):
    l=[]
    for j in range(c):
        v=int(input("Enter the number:-"))
        l.append(v)
    m1.append(l)


r2 = int(input("enter the number of rows:-"))
c2 = int(input("enter the number of columns:-"))
m2=[]
for i in range(r2):
    l=[]
    for j in range(c2):
        v=int(input("Enter the number:-"))
        l.append(v)
    m2.append(l)

if c2==r:
    multiply_matrix=[]
    for i in range(r):
        l=[]
        for j in range(c2):
            sum=0
            for k in range(c):
                sum+=m1[i][k]*m2[k][j]
            l.append(sum)
        multiply_matrix.append(l)
else:
    print("invalid input")


print("matrix 1\n")
for i in m1:
    print(i)

print("matrix 2\n")
for i in m2:
    print(i)

print("sum of matrix 1 and matrix 2\n")
for i in multiply_matrix:
    print(i)


