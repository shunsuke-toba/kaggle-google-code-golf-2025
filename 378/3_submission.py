def p(g):
 m=len(g)-2
 for z in range(m*m):
  if(z:=(t:=g[y:=z//m+1])[x:=z%m+1])and(z>g[y+(d:=(g[y+1][x]-g[y-1][x])//z)][x+(e:=(t[x+1]-t[x-1])//z)]):
   z=g[y+2*d][x+2*e]
   while y>0<x<m+1>y:g[y:=y-d][x:=x-e]=z
 return g