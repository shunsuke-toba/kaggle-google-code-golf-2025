def p(g):
 r,h,w=range,len(g),len(g[0]);_,q,x,b=max((all(1>max(r[x:x+b])for r in g[y:y+a])*a*b,g[y:y+a],x,b)for y in r(h)for x in r(w)for a in r(2,h-y+1)for b in r(2,w-x+1))
 for r in q:r[x:x+b]=[6]*b
 return g