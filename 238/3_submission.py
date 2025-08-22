def p(g):
 a=c=A=C=99;b=d=B=-1;R=range;e=enumerate;m=min;M=max
 for i,r in e(g):
  for j,v in e(r):
   if v%8:a=m(a,i);b=M(b,i);c=m(c,j);d=M(d,j)
   elif v:A=m(A,i);B=M(B,i);C=m(C,j)
 n=B-A+1;G=[r[c:d+1]for r in g[a:b+1]];t,b,l,r=G[0][1],G[-1][1],G[1][0],G[1][-1]
 for i in R(n):
  for j in R(n):
   G[i+1][j+1]=(v:=g[A+i][C+j])==8and(i^j)*-~(i+j-n)and m((i+1,t),(n-i,b),(j+1,l),(n-j,r))[1]or v
 return G