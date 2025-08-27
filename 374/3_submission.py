def p(g,x=1):
 for k in range(1584):
  i=9-k//198;r=k%-11;k%=9;g=[*map(list,zip(*g))]
  if[5]*i==g[r][k:k+i]:g[r][k:k+i]=[x]*i;x=x*4%7
 return g