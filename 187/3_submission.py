def p(g):
 a=len(g);b=len(g[0])
 def f(i,j):
  if a>i>=0<=j<b>g[i][j]==0:g[i][j]=3;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(a+b):f(i,0);f(i,b-1);f(0,i);f(a-1,i)
 return[[x or 2 for x in r]for r in g]
