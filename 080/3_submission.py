def p(g):
 R=range;h=len(g);w=len(g[0])
 for n,r in enumerate(g):
  if r==r[:1]*w:l=r[0];break
 s=n+1;m=(h+1)//s;A=[[g[i*s][j*s]for j in R(m)]for i in R(m)]
 b=4
 for y in R(m-2):
  for x in R(m-2):
   t=[A[y+i][x:x+3]for i in R(3)];u=sum(v>0 for r in t for v in r)
   if u>b:b=u;P=t;Y=y+1;X=x+1
 d=P[1][1]
 for y in R(m):
  for x in R(m):
   if A[y][x]==d and(y,x)!=(Y,X):
    for I in(-1,0,1):
     for J in(-1,0,1):
      u=y+I;v=x+J
      if m>u>=0<=v<m:A[u][v]=P[I+1][J+1]
 o=[[l]*w for _ in R(h)]
 for y in R(m):
  for x in R(m):
   v=A[y][x]
   for i in R(n):o[y*s+i][x*s:x*s+n]=[v]*n
 return o
