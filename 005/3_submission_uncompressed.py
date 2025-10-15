def p(c):
 a=b=0;h=0,1,2
 while 0in map(sum,(g:=[c[a+i][b:b+3]for i in h])+[*zip(*g)]):
  b=(b+1)%19;a+=b<1
 for d in-4,0,4:
  for e in-4,0,4:
   v=max(c[a+d+i][b+e+j]for i in h for j in h);y,x=a,b
   for j in c:
    y+=d;x+=e
    for i in h:
     for j in h:
      if g[i][j]and-1<y+i<21 and-1<x+j<21:c[y+i][x+j]=v
 return c