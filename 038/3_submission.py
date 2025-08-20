p=lambda g:[([1]*(sum(x*y==1 for r in g for x,y in zip(r,r[1:]))//2)+[0]*5)[:5]]
