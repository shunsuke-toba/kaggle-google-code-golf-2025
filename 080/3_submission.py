def p(g):
 R=range;h=len(g);n=0
 while (r:=g[n])!=r[:1]*len(r):n+=1
 s=n+1;m=-~h//s;A=[g[i*s][::s][:m]for i in R(m)];b=4
 for y in R(m-2):
  for x in R(m-2):
   t=[r[x:x+3]for r in A[y:y+3]];u=sum(map(bool,sum(t,[])))
   if u>b:b=u;P=t;c=y+1,x+1
 for y in R(m*m):
  x=y%m;y//=m
  if A[y][x]==P[1][1] and(y,x)!=c:
   for k in R(9):
    u=y+k//3-1;v=x+k%3-1
    if m>u>=0<=v<m:A[u][v]=P[k//3][k%3]
 o=[r[:1]*len(r) for _ in R(h)]
 for y in R(m*m):
  x=y%m;y//=m
  for i in R(n):o[y*s+i][x*s:x*s+n]=[A[y][x]]*n
 return o
