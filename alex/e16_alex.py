n,m=map(int,input().split())
a=[list(map(int,input().split()))for i in range(n)]
d=[]
for i in range(n):
    d.append(sum(a[i]))
print(max(d))
print(d.index(max(d))+1)
