def p(g):
 m=99;G=set()
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v:G|={i*m+j};r[j]=0
 while G:
  s=[G.pop()];k=0
  for p in s:
   for q in p+1,p-1,p+m,p-m:
    if q in G:s+=q,;G-={q}
   k+=((p+1 in s)+(p-1 in s))*((p+m in s)+(p-m in s))
  for p in s:g[p//m][p%m]=-~k*5%9
 return g