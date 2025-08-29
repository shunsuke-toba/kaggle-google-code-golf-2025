def p(g):
 b=bytes(sum(g,[]));r,c=zip(*(divmod(F(k),10)for k in set(b)-{0} for F in (b.find,b.rfind)))
 _,x,y,_=sorted(r);_,c,d,_=sorted(c)
 for r in g[x+1:y]:r[c+1:d]=[8]*(d+~c)
 return g