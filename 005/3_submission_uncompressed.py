def p(c):
 a=b=0
 while 0in map(sum,(g:=[c[a+i][b:b+3]for i in range(3)])+[*zip(*g)]):
  b=(b+1)%19;a+=b<1
 for d in-4,0,4:
  for e in-4,0,4:
   v=max(c[a+d+i][b+e+j]for i in range(3)for j in range(3));y,x=a,b
   for j in c:
    y+=d;x+=e
    for i in range(3):
     for j in range(3):
      if 0<=y+i<21>j+x>=0<g[i][j]:c[y+i][x+j]=v
 return c
