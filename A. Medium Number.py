t = int(input())
for i in range(t):
   a,b,c =map(int,input().split())
   s=[a,b,c]
   s.sort()
   print(s[1])
