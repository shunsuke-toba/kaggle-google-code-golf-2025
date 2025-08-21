def p(g):
 e=enumerate;a,b=zip(*[(i,j)for i,r in e(g)for j,x in e(r)if x==5]);return[r[b[0]:b[1]+1]for r in g[a[0]-1:a[-1]+2]]
