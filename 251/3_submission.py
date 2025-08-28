def p(g):
 n=i=len(g)
 def f(i,j):
  if 0<=i<n>j>=0==g[i][j]:g[i][j]=1;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 while i:i-=1;f(i,0);f(i,n-1);f(0,i);f(n-1,i)
 return[[v^(v<2)for v in r]for r in g]