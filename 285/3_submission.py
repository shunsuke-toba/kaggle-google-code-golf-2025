def p(g):
 n=len(o:=[*map(list,g)]);d=[(i//3-1,i%3-1)for i in range(9)if i-4]
 for k in range(n*n):
  if c:=o[y:=k//n][x:=k%n]:
   o[y][x]=0;q=[(s:=y,t:=x)]
   for y,x in q:
    for a,b in d:
     Y=y+a;X=x+b;v=Y<n>X<n and o[Y][X]
     if v==c:o[Y][X]=0;q+=(Y,X),
     elif a*b==0<v:s,t=y,x
   for a,b in d:
    if v:=o[s+a][t+b]:
     for y,x in q:g[a and 2*s+a-y or y][b and 2*t+b-x or x]=v
   o[s][t]=c
 return g