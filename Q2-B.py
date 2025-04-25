def myrange(start,stop,step):
    for i in range(start,stop,step):
        yield i

for i in myrange(1,12,2):
    print(i)