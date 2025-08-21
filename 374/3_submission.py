def p(g):
 x=1
 for k in range(1440):
  i,c,r=9-k//180,k//2%9,k//18%10;g=[*map(list,zip(*g))]
  if[5]*i==g[r][c:c+i]:g[r][c:c+i]=[x]*i;x=x*4%7
 return g