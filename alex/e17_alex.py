f = open("C://Users//Lenovo//Downloads//14 (1).txt").readlines()
k = mx = 0
for h in range(len(f)):
    for i in range(len(f[h])):
        if f[h][i-1:i+1] in 'XYZX' and k:
            k += 1
        elif f[h][i] == 'X':
            k = 1
        else:
            k = 0
        mx = max(mx, k)
print(mx)
#YZXYZWXYZ
