def p(g):
 b=bytes(sum(g,[]));m=divmod;x,y=[m(b.find(c),10)+m(b.rfind(c),10)for c in{*b}-{0}];x+=y;s=sorted;x,y,c,d=s(x[::2])[1:3]+s(x[1::2])[1:3]
 for r in g[x+1:y]:r[c+1:d]=[8]*(d+~c)
 return g