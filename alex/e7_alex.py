for i in range(1,1000):
    k=0
    for x in range(100):
        for y in range(100):
            if ((2*y-x<i) or (x+2*y>50) or (2*x+y<40))==1:
                k+=1
    if k==10000:
        print(i)
        break
    else:
        k=0
