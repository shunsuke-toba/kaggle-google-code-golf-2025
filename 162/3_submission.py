def p(g,n=323):
 if n:p(g,n-1)
 t=g[n%18:][:3];m=n//18
 for r in t*all([0]*4>r[m:m+3]for r in t):r[m:m+3]=1,1,1
 return g