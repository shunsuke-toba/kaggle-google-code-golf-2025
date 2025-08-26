def p(g):
 r=range;R=r(10,5,-1);s=next(s for i in R for j in R for y in r(len(g)-i+1)for x in r(len(g[0])-j+1)if len({*sum(s:=[L[x:x+j]for L in g[y:y+i]],[])})<3);j=len(s[0])
 for L,x in[(L,x)for L in s for x in r(j)if L[x]-s[0][0]]:
  for k in s:k[x]=L[x];L[:]=[L[x]]*j
 return s
