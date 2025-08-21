def p(g):
 o=[*map(list,g)];n=len(g);d=[(i//3-1,i%3-1)for i in range(9)if i-4]
 for k in range(n*n):
  i,j=k//n,k%n
  if(c:=o[i][j])>0:
   q=[(i,j)];A=c,;o[i][j]=-c
   for y,x in q:
    for a,b in d:
     if n>(Y:=y+a)>-1<(X:=x+b)<n and(c:=o[Y][X])>0:o[Y][X]=-c;q+=(Y,X),;A+=c,
   m=max(A,key=A.count);s=[*zip(q,A)]
   for(y,x),v in s:
    if m==v*any(n>y+a>-1<x+b<n and 0<abs(o[y+a][x+b])!=m for a,b in d if a*b==0):
     P=[(r-y,c-x)for(r,c),v in s if v==m];break
   for a,b in d:
    if n>(Y:=y+a)>-1<(X:=x+b)<n and 0<(c:=abs(o[Y][X]))!=m:
     for u,v in P:
      if n>(V:=X+(v,-v)[b&1])>-1<(U:=Y+(u,-u)[a&1])<n:g[U][V]=c
 return g
