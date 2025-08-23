def p(g):
 a=c=A=C=99;b=-1;e=enumerate
 for i,r in e(g):
  for j,v in e(r):
   if v&7:a=min(a,i);b=max(b,i);c=min(c,j)
   elif v:A=min(A,i);C=min(C,j)
 n=b-a-1;R=range(n);G=[r[c:c+n+2]for r in g[a:b+1]];k=G[0][1],G[1][-1],G[1][0],G[-1][1]
 for i in R:
  for j in R:v=g[A+i][C+j];G[i+1][j+1]=v>7 and(i-j)*(n-i-j-1)and k[(i>j)*2+(i+j>=n)]or v
 return G
