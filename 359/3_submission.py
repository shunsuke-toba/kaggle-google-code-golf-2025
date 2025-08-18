def p(g):
 h=len(g)
 for k in range(h*len(g[0])):i,j=k%h,k//h;v=g[i]+[r[j]for r in g];g[i][j]=max(v,key=v.count)
 return g