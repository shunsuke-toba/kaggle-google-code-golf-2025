def p(g):
 h=len(g);w=len(g[0]);r=range
 l=[(a*b,y,x,a,b)for a in r(2,h+1)for b in r(2,w+1)for y in r(h-a+1)for x in r(w-b+1)if all(not any(R[x:x+b])for R in g[y:y+a])]
 if l:
  _,y,x,a,b=max(l)
  for R in g[y:y+a]:R[x:x+b]=[6]*b
 return g
