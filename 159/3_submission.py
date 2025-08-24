def p(g):e=enumerate;z=sum(2in r for r in g);a,b=map(min,zip(*{(i,j)for i,r in e(g)for j,v in e(r)if v&-3}));k=z//3;r=range(z-2);return[[2]*z,*[[2,*[g[a+i//k][b+j//k]for j in r],2]for i in r],[2]*z]
