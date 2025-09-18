def p(g):
 for _ in g*4:
  for a,b,c in zip(g:=[*map(list,zip(*g))][::-1],g[1:],g[2:]):
   if(k:=(s:=bytes(b)).find(8,j:=s.rfind(2))+2)>j+3>2:b[j:k]=[2]*(k-j-3)+[8,2,8];a[k-3:k]=c[k-3:k]=[8]*3
 return g