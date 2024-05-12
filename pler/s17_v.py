f=open('14.txt')
d=[]
k=0
for i in range(9482):
    s=f.readline()
    for i in s:
        s=s.replace("XYZ", "*", 1)
    for i in s:
        if i=="*":
            k+=1
        else:
            if k:
                d.append(k)
                k=0

        
print(max(d)*3)
