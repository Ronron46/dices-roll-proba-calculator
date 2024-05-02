def product(a,b):
    res=[]
    if len(a) == 0:
        return b
    else:
        for i in range(len(a)+len(b)-1):
            res.append(0)
        for x in range(len(a)):
            for y in range(len(b)):
                res[x+y] += a[x]*b[y]
        return res