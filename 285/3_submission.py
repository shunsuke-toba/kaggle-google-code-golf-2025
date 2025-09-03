def p(g):
 n=len(o:=[*map(list,g)]);d=[(i//3-1,i%3-1)for i in range(9)if i-4]
 for k in range(n*n):
  if c:=o[y:=k//n][x:=k%n]:
   o[y][x]=0;q=[(y,x)]
   for y,x in q:
    for a,b in d:
     if (v:=o[(Y:=y+a)%n][(X:=x+b)%n])==c:o[Y][X]=0;q+=(Y,X),
     elif a*b==0<v:s,t=y,x
   for a,b in d:
    if v:=o[s+a][t+b]:
     for y,x in q:g[(y,2*s+a-y)[a%2]][(x,2*t+b-x)[b%2]]=v;o[s][t]=c
 return g