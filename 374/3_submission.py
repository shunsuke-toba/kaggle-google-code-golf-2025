def p(g,x=1):
 for k in range(1760):
  i,c,r=9-k//220,k%9,k%11-1;g=[*map(list,zip(*g))]
  if[5]*i==g[r][c:c+i]:g[r][c:c+i]=[x]*i;x=x*4%7
 return g