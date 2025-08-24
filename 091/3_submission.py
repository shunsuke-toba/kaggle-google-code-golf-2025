def p(g):e=enumerate;p=[(i,j)for i,r in e(g)for j,x in e(r)if x==5];a,b,c,d=p[0]+p[-1];return[r[b:d+1]for r in g[a-1:c+2]]
