def p(g):
 for a,b in zip(*[[r for r in g if r[i]]for i in(0,-1)]):
  if f:=8in b:a,b=b,a
  if 8in a:a[j:=a.index(8)]=4;b[:]=[8-r*3for r in b];a[f*j+1:-f|j]=b[1:j^-f]
 return g