def p(g):
 o=[*map(list,g)];n=len(g);d=[(i//3-1,i%3-1)for i in range(9)if i^4]
 for k in range(n*n):
  i,j=divmod(k,n)
  if(c:=o[i][j])>0:
   o[i][j]=-c;q=[(i,j)]
   for y,x in q:
    for a,b in d:
     Y=y+a;X=x+b
     if n>Y>-1<X<n:
      v=o[Y][X]
      if v==c:o[Y][X]=-c;q+=(Y,X),
      if v and c-abs(v) and a*b==0:s,t=y,x
   p=[(r-s,c-t)for r,c in q]
   for a,b in d:
    if(v:=o[s+a][t+b])*(v+c):
     for u,w in p:g[s+a+(u,-u)[a&1]][t+b+(w,-w)[b&1]]=abs(v)
 return g
