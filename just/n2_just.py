from itertools import *
def f(x, y, w,  z):
    return ((x <= y and (not(z))) or w) #впеисываем функцию 
for a1, a2, a3, a4, a5, a6 in product ([0,1], repeat=6): # количество а и репеат это количество пропущенных клеток
    table = [(a1, a2, 1, 0), (0, a3, a4, 1), (1, a5, 1, a6)]
    if len(table) == len(set(table)):
        for p in permutations ('xywz'):
            if [f(**dict(zip(p,r))) for r in table] == [0,0,0]: # нули это значения F
                print(*p, sep='')
