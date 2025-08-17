def p(g):
 n=len(g);N=n-1
 for t in range(N*N):
  r=t//N;c=t%N;q=g[r][c],g[r][c+1],g[r+1][c],g[r+1][c+1]
  if(m:=max(q))and 0 in q and sum(q)==3*m:
   k=q.index(0);a=k//2*2-1;b=k%2*2-1;r+=k//2+a;c+=k%2+b
   while 0<=r<n>c>=0:g[r][c]=m;r+=a;c+=b
 return g
