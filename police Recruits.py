n = int(input())
events = list(map(int, input().split()))

free= 0
crimes = 0

for i in events:
    if i == -1:
        if free > 0:
            free -= 1
        else:
           crimes += 1
    else:
        free += i

print(crimes)
