def p(g):
 r=lambda g:[*map(list,zip(*g[::-1]))];c=0
 while g[6][0]^2:g=r(g);c+=1
 f=8 in g[-1];s=g[-f].index(8);w=g[0].index(0)
 for i,h in enumerate(g):k=w+abs(s-(i,11-i)[f]-w);h[k]=h[k]or 3
 while c%4:g=r(g);c+=1
 return g
