def p(a):
 w=len(a[0])-1
 for i in range(10):a[~i][w-abs(i%(w+w)-w)]=1
 return a