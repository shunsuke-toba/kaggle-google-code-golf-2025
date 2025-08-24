def p(g,R=range):
 def f(x,y):
  try:
   if x>-1<y and g[x][y]:g[x][y]=0;f(x+1,y);f(x-1,y);f(x,y+1);f(x,y-1)
  except:0
 n=sum(f(i,j)or 1 for i in R(len(g))for j in R(len(g[0]))if g[i][j])
 return[[8*(i==j)for j in R(n)]for i in R(n)]
