def p(g):
 for _ in g*4:
  for a,b,c in zip(g:=[*map(list,zip(*g))][::-1],g[1:],g[2:]):
   if(k:=(s:=bytes(b)).find(8,j:=s.rfind(2))-1)>j>~0:b[j:k+3]=[2]*(k-j)+[8,2,8];a[k:k+3]=c[k:k+3]=[8]*3
 return g