def p(g):
 r=lambda:[*map(list,zip(*g[::-1]))];c=4
 while g[6][0]^2:g=r();c-=1
 f=8 in g[-1];w=g[0].index(0)
 for i,h in enumerate(g):k=w+abs(g[-f].index(8)-(i,11-i)[f]-w);h[k]=h[k]or 3
 for _ in'0'*c:g=r()
 return g
