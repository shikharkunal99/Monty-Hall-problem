import random

TIMES=100000
without_switch=0
with_switch=0


for _ in range(TIMES):
    a=["goat" for i in range(4)]
    x=random.randint(1,3)  ##car is at positon x
    a[x]="car"

    y=random.randint(1,3) ##initial choice of user


    ## position ans is shown to contain goat
    seq = range(1,4)
    random.shuffle(seq)
    for i in seq:
        if i!=x and i!=y:
            ans=i
            break
    

    ##switching
    random.shuffle(seq)
    for i in seq:
        if i!=y and i!=ans:
            other=i
            break
    if a[other]=="car":
        with_switch+=1
    
    ##without switching
    if a[y]=="car":
        without_switch+=1
    

print "with switching, wins=",with_switch
print "without switching, wins=",without_switch
print "probability of winning after switching is",((100.0*with_switch)/TIMES)
print "probability of winning without switching is",((100.0*without_switch)/TIMES)
