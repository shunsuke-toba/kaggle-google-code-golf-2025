def p(g):
 n=len(g)
 for s in range(1,n+1):
  d={}
  if all((v:=g[k//n][k%n])<1 or d.setdefault((k//n%s,k%n%s),v)==v for k in range(n*n)):
   return[[d[i%s,j%s]for j in range(n)]for i in range(n)]
