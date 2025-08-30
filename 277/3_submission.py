def p(g):
 def f(i,j,c=1,d=8):
  g[i][j]=c;return 1+sum(f(x,y,c,d)for s in range(9)if-1<(x:=i+s//3-1)<10>(y:=j+s%3-1)>-1<g[x][y]==d)
 f(*min((f(i,j),i,j)for k in range(99)if g[i:=k//10][j:=k%10]==8)[1:],2,1);return g