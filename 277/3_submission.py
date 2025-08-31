def p(g,r=range(9)):
 def f(i,j,d=8):g[i][j]=-d%3;return-~sum(f(x,y,d)for s in r if-1<(x:=i+s//3-1)<10>(y:=j+s%3-1)>-1<g[x][y]==d)
 f(*min((f(i,j),i,j)for i in r for j in r if g[i][j]>7)[1:],1);return g