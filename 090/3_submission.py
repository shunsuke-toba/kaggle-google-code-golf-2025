def p(g):
 r=range;h=len(g);w=len(g[0]);_,y,x,a,b=max((a*b,y,x,a,b)for y in r(h)for x in r(w)for a in r(2,h-y+1)for b in r(2,w-x+1)if sum(max(R[x:x+b])for R in g[y:y+a])<1)
 for R in g[y:y+a]:R[x:x+b]=[6]*b
 return g