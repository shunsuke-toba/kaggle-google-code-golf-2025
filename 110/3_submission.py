def p(g):
 for r in g:r[:]=map(max,*[t for t in g if 1>any(a*b*(a-b)for a,b in zip(r,t))])
 return g