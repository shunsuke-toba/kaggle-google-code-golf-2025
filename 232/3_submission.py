def p(g):
 for r in g:
  for i in range(1,len(r)):
   if(l:=r[i-1]):r[i]=[5,r[i-2]][l==5]
 return g
