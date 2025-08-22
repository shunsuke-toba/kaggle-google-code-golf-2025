def p(g):
 h=any(r.count(3)>1 for r in g);s=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==2];d=2*h
 for i,j in s:g[i][j]=0
 for i,j in s:g[i+2-d][j+d]=2
 return g
