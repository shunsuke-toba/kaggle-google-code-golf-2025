def p(g):
 r=lambda g:[*map(list,zip(*g[::-1]))]
 c=0
 while g[6][0]-2:g=r(g);c+=1
 f=8 in g[-1];t=g[-1]if f else g[0];s=t.index(8);w=g[0].count(2)
 for i,h in enumerate(g):j=abs(s-(i,11-i)[f]-w)+w;h[j]=h[j]or 3
 for c in range(-c%4):g=r(g)
 return g
