def p(g):
 g=[r+[0]for r in g]+[[0]*10];L=[];R=range(10)
 for r in R:
  for c in R:
   if g[r][c]>4>g[r-1][c]|g[r][c-1]:
    d=g[r+1][c]>4;i=0
    while g[r+i*d][c+i*(1-d)]>4:i+=1
    L+=((i,r,c,d),)
 for(l,r,c,d),k in zip(sorted(L),(2,4,1)):
  for i in range(l):g[r+i*d][c+i*(1-d)]=k
 return [r[:10]for r in g][:10]
