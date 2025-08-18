def p(G):
 A=C=a=c=99;B=b=d=-1;m=min;M=max;e=enumerate;r=range
 for i,k in e(G):
  for j,v in e(k):
   if v%8:a=m(a,i);b=M(b,i);c=m(c,j);d=M(d,j)
   elif v:A,B,C=m(A,i),M(B,i),m(C,j)
 g=[r[c:d+1]for r in G[a:b+1]]
 X,Y,Z,W=g[0][1],g[-1][1],g[1][0],g[1][-1]
 for i in r(n:=B-A+1):
  for j in r(n):
   if (v:=G[A+i][C+j])==8and(i^j)*-~(i+j-n):v=m((i+1,X),(n-i,Y),(j+1,Z),(n-j,W))[1]
   g[i+1][j+1]=v
 return g
