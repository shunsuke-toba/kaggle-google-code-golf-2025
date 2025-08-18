def p(g):
 R=range;E=enumerate;h=len(g);w=len(g[0]);m=0
 for a in R(h):
  for b in R(a+1,h+1):
   for c in R(w):
    v=g[a][c]
    for d in R(c+1,w+1):
     if(t:=(b-a)*(d-c))>m and all(g[a][x]==v==g[b-1][x]for x in R(c,d))and all(g[y][c]==v==g[y][d-1]for y in R(a,b)):m=t;A,B,C,D,V=a,b,c,d,v
 o=[r[C:D]for r in g[A:B]];g=[r[:]for r in o];c=V
 for i,r in E(o):
  for j,v in E(r):
   if v-c:
    for k in g:k[j]=v
    g[i]=[v]*(D-C)
 return g
