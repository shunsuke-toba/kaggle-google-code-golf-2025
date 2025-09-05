def p(g):
 for z in range((m:=~-len(g))*m):
  if 0<(z:=(t:=g[y:=z//m])[x:=z%m])>g[a:=y+(d:=(g[y+1][x]-g[y-1][x])//z)][b:=x+(e:=(t[x+1]-t[x-1])//z)]:
   while m>y>0<x<m:g[y:=y-d][x:=x-e]=g[a+d][b+e]
 return g