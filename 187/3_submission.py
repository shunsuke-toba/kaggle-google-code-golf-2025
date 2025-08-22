def p(g):
 a=len(g);b=len(g[0])
 def f(i,j):
  if a>i>=0<=j<b and g[i][j]<1:
   g[i][j]=3;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(a*b):j=i%b;i//=b;i*j*(i-a+1)*(j-b+1)<1 and f(i,j)
 return [[x or 2 for x in r]for r in g]
