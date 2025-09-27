def p(g):
 a=min(i for i,r in enumerate(g)for j,v in enumerate(r)if v%8)
 c=min(j for i,r in enumerate(g)for j,v in enumerate(r)if v%8)
 b=-min(-i for i,r in enumerate(g)for j,v in enumerate(r)if v%8)
 e=min(j for i,r in enumerate(g)for j,v in enumerate(r)if v==8)
 d=min(i for i,r in enumerate(g)for j,v in enumerate(r)if v==8)
 s=[(i-d,j-e)for i,r in enumerate(g)for j,v in enumerate(r)if v==8]
 n=b-a-2;g=[r[c:c+b-a+1]for r in g[a:b+1]];t=g[-1][1],g[1][0],g[1][-1],g[0][1]
 for i,j in s:g[i+1][j+1]=(i-j)*(i+j-n)and t[(i<j)*2+(i+j<n)]or 8
 return g