def p(g):
 b=bytes(sum(g,[]));r,(_,a,b,_)=map(sorted,zip(*{divmod(f(k),10)for k in b for f in(b.find,b.rfind)if k}))
 for r in g[r[1]+1:r[2]]:r[a+1:b]=[8]*(b+~a)
 return g