def p(g):
 r=range;l=len;R=r(10,5,-1);s=next(s for i in R for j in R for y in r(l(g)-i+1)for x in r(l(g[0])-j+1)if l({*sum(s:=[L[x:x+j]for L in g[y:y+i]],[])})<3);j=l(s[0])
 for L,x in[(L,x)for L in s for x in r(j)if L[x]-s[0][0]]:
  for c in s:c[x]=L[x];L[:]=[L[x]]*j
 return s