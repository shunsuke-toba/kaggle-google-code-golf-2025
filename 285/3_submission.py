def p(g):
 o=[*map(list,g)];n=len(g);d=[(i//3-1,i%3-1)for i in range(9)if i-4]
 for k in range(n*n):
  if(c:=o[i:=k//n][j:=k%n])>0:
   q=[(i,j)];A=c,;o[i][j]=-c
   for y,x in q:
    for a,b in d:
     if n>(Y:=y+a)>-1<(X:=x+b)<n and(c:=o[Y][X])>0:o[Y][X]=-c;q+=(Y,X),;A+=c,
   m=max(A,key=A.count);s=[*zip(q,A)]
   for(y,x),v in s:
    if m==v*any(-m!=o[y+a][x+b]!=0 for a,b in d if a*b==0):
     p=[(r-y,c-x)for(r,c),v in s if v==m];break
   for a,b in d:
    if 0>(c:=o[y+a][x+b])!=-m:
     for u,v in p:g[y+a+(u,-u)[a&1]][x+b+(v,-v)[b&1]]=-c
 return g
