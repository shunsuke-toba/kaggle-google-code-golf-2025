def p(g):
 o=[*map(list,g)];n=len(g);d=[(i//3-1,i%3-1)for i in range(9)if i^4]
 for k in range(n*n):
  if(c:=o[i:=k//n][j:=k%n])>0:
   o[i][j]=-c
   for y,x in(q:=[(i,j)]):
    for a,b in d:
     if n>(Y:=y+a)>-1<(X:=x+b)<n>c==o[Y][X]:o[Y][X]=-c;q+=(Y,X),
   y,x=next(((y,x)for y,x in q if any(-c!=o[y+a][x+b]!=0 for a,b in d if a*b==0)),q[0]);p=[(r-y,c-x)for r,c in q]
   for a,b in d:
    for u,w in p:g[y+a+(u,-u)[a&1]][x+b+(w,-w)[b&1]]|=abs(v:=o[y+a][x+b])*(v+c!=0)
 return g
