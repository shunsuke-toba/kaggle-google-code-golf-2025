def p(g):
 m=len(g)-2
 for z in range(m*m):
  if(c:=(t:=g[y:=z//m+1])[x:=z%m+1])and(d:=(g[y+1][x]-g[y-1][x])//c)*(e:=(t[x+1]-t[x-1])//c)*(g[y+d][x+e]<c):
   c=g[y+2*d][x+2*e]
   while y>0<x<m+1>y:g[y:=y-d][x:=x-e]=c
 return g