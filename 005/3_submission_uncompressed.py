def p(g):
 A=0,1,2;a=b=0
 while 0in map(sum,(C:=[g[a+i][b:b+3]for i in A])+[*zip(*C)]):
  b=-~b%19;a+=b<1
 for d in-4,0,4:
  for e in-4,0,4:
   v=max(g[a+d+i][b+e+j]for i in A for j in A);y,x=a,b
   for _ in g:
    y+=d;x+=e
    for i in A:
     for j in A:
      if 0<=y+i<21>j+x>=0<C[i][j]:g[y+i][x+j]=v
 return g