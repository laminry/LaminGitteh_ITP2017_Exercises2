n = 10
list = []
a = b = 0
c = 1

for i in range (n):
    a = b + c
    c = b
    b = a
    list.append(str(a))

print(",".join(list))