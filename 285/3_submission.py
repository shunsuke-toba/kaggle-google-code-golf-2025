def p(g):
 o=[*map(list,g)];n=len(g);d=[(i//3-1,i%3-1)for i in range(9)if i^4]
 for k in range(n*n):
  if(c:=o[i:=k//n][j:=k%n])>0:
   q=[(i,j)];C=c,;o[i][j]=-c
   for y,x in q:
    for a,b in d:
     if n>(Y:=y+a)>-1<(X:=x+b)<n and(c:=o[Y][X])>0:o[Y][X]=-c;q+=(Y,X),;C+=c,
   for(y,x),v in zip(q,C):
    if C.count(v)-1 and any(-v!=o[y+a][x+b]!=0 for a,b in d if a*b==0):
     p=[(r-y,c-x)for(r,c),w in zip(q,C)if w==v];m=v;break
   for a,b in d:
    if 0>(c:=o[y+a][x+b])!=-m:
     for u,v in p:g[y+a+(u,-u)[a&1]][x+b+(v,-v)[b&1]]=-c
 return g
