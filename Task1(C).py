arr = [7,8,9,10,16,43]
a = [0]*len(arr)
print(0,1)
p1 = int(input())
print(1,2)
p2 = int(input())
Pr = p1*p2
print(Pr)
for i in range(3):
    Pr = Pr/arr[i]
    print(Pr)
a[1] = Pr
a[0] = p1/Pr
a[2] = p2/Pr

print(3,4)
p3 = int(input())
print(4,5)
p4 = int(input())
P = p3*p4
for i in range(3,6):
    P = P/arr[i]
a[4] = P
a[3] = p3/P
a[5] = p4/P
print(a)
