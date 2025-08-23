def p(g):
 b=bytes(sum(g,[]));a,b=sorted(divmod(b.find(c),10)+divmod(b.rfind(c),10)for c in {*b}-{0});x,y,c,d=(a[2]+1,b[0],max(a[1],b[1])+1,min(a[3],b[3]))if a[2]<b[0]else(max(a[0],b[0])+1,min(a[2],b[2]),min(a[3],b[3])+1,max(a[1],b[1]))
 for r in g[x:y]:r[c:d]=[8]*(d-c)
 return g
