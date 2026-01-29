n = int(input())
y = 0
x = [int(i) for i in str(n)]
for i in x:
    if i == 4 or i == 7:
        y += 1
if y == 4 or y == 7:
    print("YES")
else:
    print("NO")
