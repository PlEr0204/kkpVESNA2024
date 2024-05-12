for A in range(1,1000):
    k=0
    for x in range(100):
        if ((x&55==0)or(x&10!=0)or(x&A!=0))==1:
            k+=1
    if k==100:
        print(A)
        break
