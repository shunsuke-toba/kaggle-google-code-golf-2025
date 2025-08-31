def p(g):
 n=len(o:=[*map(list,g)]);d=[(i//3-1,i%3-1)for i in range(9)if i^4]
 for k in range(n*n):
  if(c:=o[y:=k//n][x:=k%n])>0:
   o[y][x]=-c;q=[(y,x)]
   for y,x in q:
    for a,b in d:
     Y=y+a;X=x+b;v=n>Y>-1<X<n and o[Y][X]
     if v==c:o[Y][X]=-c;q+=(Y,X),
     elif a*b==0!=v!=-c:s,t=y,x
   for a,b in d:
    if(v:=o[s+a][t+b])*(v+c):
     for y,x in q:g[s+a+[y-s,s-y][a&1]][t+b+[x-t,t-x][b&1]]=abs(v)
 return g