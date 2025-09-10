def p(g):
 r=range;l=len;R=r(10,5,-1);s,j=[(s,j)for i in R for j in R for y in r(l(g)-i)for x in r(l(g[0])-j)if 3>l({*sum(s:=[L[x:x+j]for L in g[y:y+i]],[])})][0]
 for L,x in[(L,x)for L in s for x in r(j)if L[x]-L[0]]:
  for c in s:c[x]=v=L[x];L[:]=[v]*j
 return s