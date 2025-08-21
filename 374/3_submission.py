def p(g):
 x=1
 for k in range(1600):
  i,c,r=9-k//200,k%10,k//10%10
  if g[r][c:c+i]==[5]*i:g[r][c:c+i]=[x]*i;x=x*4%7
  if~k%100:g=[*map(list,zip(*g))]
 return g
