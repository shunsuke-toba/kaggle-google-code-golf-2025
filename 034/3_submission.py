def p(g):
 for i in range(81):
  r=i//9;c=i%9;a=g[r][c]
  if a:
   t=a,g[r][c+1],g[r+1][c],g[r+1][c+1];o=r,c
   for x in t:
    if x-2:break
   for j in 0,1,2,3:
    if t[j]==2:
     r,c=o
     while 9>r>-2<c<9:
      for k in 0,1,2,3:
       u=r+k//2;v=c+k%2
       if 9>u>-1<v<9:g[u][v]=x
      r+=j//2*2-1;c+=j%2*2-1
   return g
