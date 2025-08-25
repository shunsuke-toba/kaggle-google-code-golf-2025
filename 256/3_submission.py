def p(g):
 a=g.index(max(g));b=sum(g[a])//2+a
 for y in range(b):g[y][:b-y]=[2+(y<a)-(y>a)]*(b-y)
 return g