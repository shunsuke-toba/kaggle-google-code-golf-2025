def p(a):
 w=len(a[0])-1;i=10
 while i:i-=1;a[~i][~abs(i%(w*2)-w)]=1
 return a