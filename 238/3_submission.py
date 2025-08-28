def p(g):
 a=c=d=e=99;f=enumerate;[v%8and(a:=min(a,b:=i),c:=min(c,j))or v and(d:=min(d,i),e:=min(e,j))for i,r in f(g)for j,v in f(r)];n=b+~a;G=[x[c:c+n+2]for x in g[a:b+1]]
 for k in range(n*n):i=k//n;j=k%n;v=g[d+i][e+j];G[i+1][j+1]=v*(i-j)*~(i+j-n)and(G[-1][1],G[1][-1],G[1][0],G[0][1])[(i<j)+(i+j<n)*2]or v
 return G