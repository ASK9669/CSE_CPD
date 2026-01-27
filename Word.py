s= str(input())
l = 0
u = 0
for ch in s:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l+= 1
if l>= u:
    print(s.lower())
else:
    print(s.upper())
