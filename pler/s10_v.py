#Такое же как и 7 и 8
for A in range(1,1000):
    k=0
    for x in range(100):
        if (x&55==0)or(x&10!=0)or(x&A!=0):
            k+=1
    if k==100:
        print(A)
        break
"""
Определите наименьшее натуральное число A, такое что выражение
(x&55=0)∨(x&10≠0)∨(x&A≠0)

тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной x)?"""
