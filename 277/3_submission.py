def p(g):
 def f(i,j,d=8):g[i][j]=-d%3;return-~sum(f(x,y,d)for s in range(9)if-1<(x:=i+s//3-1)<10>(y:=j+s%3-1)>-1<g[x][y]==d)
 f(*min((f(i,j),i,j)for k in range(99)if g[i:=k//10][j:=k%10]>7)[1:],1);return g