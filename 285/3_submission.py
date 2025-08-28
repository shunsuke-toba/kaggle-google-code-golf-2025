def p(g):
 o=[*map(list,g)];n=len(g);d=[(i//3-1,i%3-1)for i in range(9)if i^4]
 for k in range(n*n):
  i=k//n;j=k%n;c=o[i][j]
  if c>0:
   o[i][j]=-c;q=[(i,j)]
   for y,x in q:
    for a,b in d:
     Y=y+a;X=x+b;v=n>Y>-1<X<n and o[Y][X]
     if v==c:o[Y][X]=-c;q+=(Y,X),
     elif v*(c-abs(v))*(a*b==0):s,t=y,x
   for a,b in d:
    if(v:=o[s+a][t+b])*(v+c):
     for y,x in q:g[s+a+((y-s,s-y)[a&1])][t+b+((x-t,t-x)[b&1])]=abs(v)
 return g