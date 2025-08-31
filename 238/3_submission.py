def p(g):
 a=c=d=e=99;f=enumerate;m=min;[v-8and(a:=m(a,b:=i),c:=m(c,j))or(d:=m(d,i),e:=m(e,j))for i,r in f(g)for j,v in f(r)if v];n=b+~a;G=[r[c:c+n+2]for r in g[a:b+1]]
 for k in range(n*n):i=k//n;k%=n;v=g[d+i][e+k];G[i+1][k+1]=v*(i^k)*(n+~i-k)and((G[-1][1],G[1][0]),(G[1][-1],G[0][1]))[i<k][i+k<n]or v
 return G