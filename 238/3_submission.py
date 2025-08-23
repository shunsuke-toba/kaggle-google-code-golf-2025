def p(g):
 a=c=A=C=99;b=d=B=-1;R=range;e=enumerate
 for i,r in e(g):
  for j,v in e(r):
   if v%8:a=min(a,i);b=max(b,i);c=min(c,j);d=max(d,j)
   elif v:A=min(A,i);B=max(B,i);C=min(C,j)
 n=B-A+1;G=[r[c:d+1]for r in g[a:b+1]];k=[G[0][1],G[1][-1],G[1][0],G[-1][1]]
 for i in R(n):
  for j in R(n):
   v=g[A+i][C+j]
   G[i+1][j+1]=v==8and(i-j)*(i+j+1-n)and k[(i>j)*2+(i+j>n-1)]or v
 return G
