def p(g):
 for z in range((m:=~-len(g))*m):
  if (t:=g[y:=z//m])[x:=z%m]>g[a:=y+(d:=(g[y+1][x]>0)-(g[y-1][x]>0))][b:=x+(e:=(t[x+1]>0)-(t[x-1]>0))]:
   while m>y>0<x<m:g[y:=y-d][x:=x-e]=g[a+d][b+e]
 return g