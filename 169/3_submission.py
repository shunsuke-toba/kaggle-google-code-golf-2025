def p(g,k=110):
 f=lambda n:(x:=n//11)|9-x|9-(y:=n%11)>C<g[x][y]and(exec('g[x][y]=C')or-~f(n+11)+f(n-11)+f(n+1)+f(n-1))
 while k:C=4;C=5-f(k:=k-1);f(k)
 return g