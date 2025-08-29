def p(g,t=1):
 for k in range(1584):
  i=9-k//198;r=k%-11;k%=9;g=[*map(list,zip(*g))]
  if[5]*i==g[r][k:k+i]:g[r][k:k+i]=[t%7]*i;t*=4
 return g