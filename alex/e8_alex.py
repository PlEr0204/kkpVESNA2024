for i in range(1,1000):
    k=0
    for x in range(100):
        if(( x%45==0 and (not(x%15==0)))<=(not(i)))==1:
            print(i)
            k=1
            break
    if k==1:
        break