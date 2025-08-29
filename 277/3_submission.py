def p(g):
 v=8
 def f(i,j,c):
  g[i][j]=c;return 1+sum(f(x,y,c)for s in range(9)if-1<(x:=i+s//3-1)<10>(y:=j+s%3-1)>-1<g[x][y]==v)
 b=min((f(i,j,1),i,j)for k in range(99)if g[i:=k//10][j:=k%10]==v)[1:]
 v=1;f(*b,2)
 return g