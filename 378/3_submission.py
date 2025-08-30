def p(g):
 for z in range((m:=len(g)-1)**2):
  if (z:=(t:=g[y:=z//m])[x:=z%m])and z>g[y+(d:=(g[y+1][x]-g[y-1][x])//z)][x+(e:=(t[x+1]-t[x-1])//z)]:
   z=g[y+2*d][x+2*e]
   while m>y>0<x<m:g[y:=y-d][x:=x-e]=z
 return g