def p(g):
 def f(i,j,t=0):
  if -1<i<10>j>-1<g[i][j]-5<4+t:
   g[i][j]=t or 9
   return 1+f(i+1,j,t)+f(i-1,j,t)+f(i,j+1,t)+f(i,j-1,t)
  return 0
 k=99
 while~k:
  i,j=k//10,k%10;k-=1
  t=5-f(i,j);f(i,j,t)
 return g