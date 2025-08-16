def p(g,c=[0,2,0,4,6,3,0,1,0]):
 m=len(g);n=len(g[0]);k=0
 def f(i,j):
  if 0<=i<m and 0<=j<n and g[i][j]<1:
   g[i][j]=v or 9;f(i+1,j);f(i-1,j);f(i,j+1);f(i,j-1)
 for i in range(m):
  for j in range(n):
   if g[i][j]<1:
    v=c[k%9];f(i,j);k+=1
 return [[x%9 for x in r] for r in g]
