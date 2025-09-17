def p(g):
 a=c=d=e=99;s=[];f=enumerate;m=min;[v-8and(a:=m(a,b:=i),c:=m(c,j))or(s.append((i,j)),d:=m(d,i),e:=m(e,j))for i,r in f(g)for j,v in f(r)if v];n=b+~a;o=n-1;g=[r[c:c+n+2]for r in g[a:b+1]];t=g[-1][1],g[1][0],g[1][-1],g[0][1]
 for i,j in s:i-=d;j-=e;g[i+1][j+1]=(i==j or i+j==o)and 8 or t[(i<j)*2+(i+j<o)]
 return g
