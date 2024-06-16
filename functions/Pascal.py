def pascal(n,k,tab):
    if n <= len(tab):
        return (tab[n][k])
    else:
        for x in range(len(tab),n+1):
            a=[]     
            for y in range(int(x/2)+1):
                if y == 0:
                    a.append(1)
                elif y == x:
                    a.append(1)
                else:
                    a.append(tab[x-1][y-1] + tab[x-1][y])
            if x%2 ==0:
                for y in range(x-int(x/2)):
                    a.append(a[int(x/2)-1-y])
            elif x%2 != 0:
                for y in range(int(x/2)+1):
                    a.append(a[int(x/2)-y])            
            tab.append(a)
        return tab[n][k]