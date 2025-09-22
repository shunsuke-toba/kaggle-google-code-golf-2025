def p(g,k=160):
 f=lambda n:(x:=n>>4)|9-x|9-(y:=n&15)>C<g[x][y]and(exec('g[x][y]=C')or-~f(n+16)+f(n-16)+f(n+1)+f(n-1))
 while k:C=4;C=5-f(k:=k-1);f(k)
 return g