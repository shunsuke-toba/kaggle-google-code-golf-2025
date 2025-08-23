def p(g):
 b=bytes(sum(g,[]));a,b=[divmod(b.find(c),10)+divmod(b.rfind(c),10)for c in{*b}-{0}]
 x,y=sorted(a[::2]+b[::2])[1:3];x+=1;c,d=sorted(a[1::2]+b[1::2])[1:3];c+=1
 for r in g[x:y]:r[c:d]=[8]*(d-c)
 return g
