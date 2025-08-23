def p(g):
 h=len(g)
 def f(i,j):
  if i*i<h*h>j*j and g[i][j]<1:g[i][j]=1;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(h):f(i,0);f(i,-1);f(0,i);f(-1,i)
 return[[v^(v<2)for v in r]for r in g]
