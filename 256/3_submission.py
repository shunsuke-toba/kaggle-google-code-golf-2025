def p(g):
 c=sum(m:=max(g))//2;b=c+g.index(m)
 for r in g:r[:b]=[2+(b>c)-(b<c)]*b;b-=b>0
 return g