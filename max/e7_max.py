for a in range(500):
    f = False
    for x in range(500):
        for y in range(500):
            q = 2*y - x < a
            w = x + 2*y > 50
            e = 2*x + y < 40
            if (q or w or e)==0:
                f = True
                break
        if f:
            break
    else:
        print(a)
"""
Укажите наименьшее целое значение А, при котором выражение
(2y–x<A)∨(x+2y>50)∨(2x+y<40)

истинно для любых целых положительных значений x и y.
"""