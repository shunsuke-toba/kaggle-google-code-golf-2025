def p(g,A=range):
 c=len(g);E=len(g[0])
 def f(x,y):g[x][y]=0;[f(x+a,y+b)for a,b in((1,0),(-1,0),(0,1),(0,-1))if c>x+a>-1<y+b<E and g[x+a][y+b]]
 k=sum(f(i,j)or 1 for i in A(c)for j in A(E)if g[i][j])
 return[[8*(i==j)for j in A(k)]for i in A(k)]