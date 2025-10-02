def p(g,n=323):
 if n:p(g,n-1)
 t=g[n%18:][:3];n//=18
 for r in t*all([0]*4>r[n:n+3]for r in t):r[n:n+3]=1,1,1
 return g