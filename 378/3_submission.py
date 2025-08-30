def p(g):
 for z in range((m:=len(g)-2)**2):
  if 0<(z:=(t:=g[y:=z//m+1])[x:=z%m+1])>g[y+(d:=(g[y+1][x]-g[y-1][x])//z)][x+(e:=(t[x+1]-t[x-1])//z)]:
   z=g[y+2*d][x+2*e]
   while y>0<x<m+1>y:g[y:=y-d][x:=x-e]=z
 return g