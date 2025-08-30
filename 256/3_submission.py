def p(g):
 c=sum(m:=max(g))//2;b=y=c+g.index(m)
 while b:g[y-b][:b]=[2+(b>c)-(b<c)]*b;b-=1
 return g