def p(g):
 s,j=[(s,j)for i in range(10,5,-1) for j in range(10,5,-1) for y in range(len(g)-i)for x in range(len(g[0])-j)if 3>len({*sum(s:=[L[x:x+j]for L in g[y:y+i]],[])})][0]
 for L,x in[(L,x)for L in s for x in range(j)if L[x]-L[0]]:
  for c in s:c[x]=v=L[x];L[:]=[v]*j
 return s
