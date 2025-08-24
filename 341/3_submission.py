def p(g):
 b=bytes(sum(g,[]));x,y=[divmod(b.find(c),10)+divmod(b.rfind(c),10)for c in{*b}-{0}];x+=y;x,y,c,d=sorted(x[::2])[1:3]+sorted(x[1::2])[1:3]
 for r in g[x+1:y]:r[c+1:d]=[8]*(d+~c)
 return g
