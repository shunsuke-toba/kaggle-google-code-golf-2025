def p(g):
 E=enumerate
 a,b=zip(*[(i,j)for i,r in E(g)for j,x in E(r)if x==5])
 return[r[min(b):max(b)+1]for r in g[a[0]-(a[0]>0):a[-1]+2]]
