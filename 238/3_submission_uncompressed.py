def p(g):
 f=enumerate
 a=min(i for i,r in f(g)for j,v in f(r)if v and v-8)
 b=max(i for i,r in f(g)for j,v in f(r)if v and v-8)
 c=min(j for i,r in f(g)for j,v in f(r)if v and v-8)
 d=min(i for i,r in f(g)for j,v in f(r)if v==8)
 e=min(j for i,r in f(g)for j,v in f(r)if v==8)
 S=[(i,j)for i,r in f(g)for j,v in f(r)if v==8]
 n=b-a-2;g=[r[c:c+b-a+1]for r in g[a:b+1]];t=g[-1][1],g[1][0],g[1][-1],g[0][1]
 for i,j in S:i-=d;j-=e;g[i+1][j+1]=(i==j or i+j==n)and 8 or t[(i<j)*2+(i+j<n)]
 return g