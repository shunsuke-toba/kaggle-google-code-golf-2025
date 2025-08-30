def p(g):
 m=max(g);c=sum(m)//2;b=y=c+g.index(m)
 while b:g[y-b][:b]=[2+(b>c)-(b<c)]*b;b-=1
 return g