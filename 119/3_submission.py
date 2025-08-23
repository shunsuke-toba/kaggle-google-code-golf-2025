def p(g):
 r=lambda g:[*map(list,zip(*g[::-1]))];c=0
 while g[6][0]-2:g=r(g);c+=1
 f=8in g[-1];s=g[f*-1].index(8);w=g[0].count(2)
 for i,h in enumerate(g):j=w+abs(s-(i,11-i)[f]-w);h[j]=h[j]or 3
 for _ in[0]*(-c%4):g=r(g)
 return g