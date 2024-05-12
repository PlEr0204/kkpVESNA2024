def f(n, m):
  for i in range(n):
    if m[i][i] == 1:
      return "NO"
  for i in range(n):
    for j in range(i + 1, n): #или просто поставить n
      if m[i][j] != m[j][i]:
        return "NO"

  return "YES"
n = int(input())
m = []
for i in range(n):
  row = list(map(int, input().split()))
  m.append(row)
print(f(n, m))
