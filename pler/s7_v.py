A=[]
for i in range(1,1000):
    k=0
    for x in range(100):
        for y in range(100):
            if ((2*y-x<i) or (x+2*y>50) or (2*x+y<40))==1:
                k+=1
    if k==10000:
        print(i)
        A.append(i)
    else:
        k=0
print(A)
"""
Укажите наименьшее целое значение А, при котором выражение
(2y–x<A)∨(x+2y>50)∨(2x+y<40)

истинно для любых целых положительных значений x и y.
"""
