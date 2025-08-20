def p(a):
 w=len(a[0])-1;i=-w
 for r in a[::-1]:r[abs(i%(w+w)-w)]=1;i+=1
 return a
