def p(g,t=1):
 for k in range(1584):
  i=9-k//198;*g,=map(list,zip(*g));h=g[k%-11];k%=9
  if[5]*i==h[k:k+i]:h[k:k+i]=[t%7]*i;t*=4
 return g