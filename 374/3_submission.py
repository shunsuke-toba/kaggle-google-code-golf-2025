def p(g):
 x=1
 for k in range(1440):
  i,c,r=9-k//180,k%9,k//9%10
  if[5]*i==g[r][c:c+i]:g[r][c:c+i]=[x]*i;x=x*4%7
  if~k%90:g=[*map(list,zip(*g))]
 return g