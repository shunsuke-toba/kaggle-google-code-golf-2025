def p(g):e=enumerate;y,x,v=zip(*((i,j,v)for i,r in e(g)for j,v in e(r)if v));a,b={*v};return[[a^b^k for k in r[min(x):max(x)+1]]for r in g[min(y):max(y)+1]]
