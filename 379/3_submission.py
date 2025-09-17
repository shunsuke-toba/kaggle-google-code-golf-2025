def p(g):
 for _ in g*4:
  for a,b,c in zip(g,g[1:],g[2:]):
   if(k:=(s:=bytes(b)).find(8,j:=s.rfind(2)))>j+1>0:b[j:k+2]=[2]*(k+~j)+[8,2,8];a[k-1:k+2]=c[k-1:k+2]=[8]*3
  g=[*map(list,zip(*g))][::-1]
 return g