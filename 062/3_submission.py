def p(g):
 d={}
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v:d.setdefault(v,[]).append((y,x))
 a,b=sorted(d.values(),key=len);c=g[b[0][0]][b[0][1]]
 y,x=zip(*b);Y=min(y);Z=max(y);X=min(x);W=max(x)
 y,x=zip(*a);A=min(y);B=max(y);C=min(x)
 o=[[3]*len(g[0])for _ in g]
 if Z>=A<=B>=Y:
  L=2*W+1 if C>W else 2*X-1
  for y,x in b:o[y][x]=o[y][L-x]=c
 else:
  L=2*Z+1 if A>Z else 2*Y-1
  for y,x in b:o[y][x]=o[L-y][x]=c
 return o
