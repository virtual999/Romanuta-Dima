a = int(input())
b = int(input())
v = str(a)
r = str(b)
t = len(v)
y = len(r)
if a % 7 == 0:
    if t == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
if b % 7 == 0:
    if y == 4:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
