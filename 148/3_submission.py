def p(g):
 p=[r for r in g if r[0]or r[-1]]
 for a,b in zip(p,p[len(p)//2:]):
  if 8in a:a[j:=a.index(8)]=4;f=a[0]==0;b[:]=[8-r*3for r in b];a[f*j+1:-f|j]=b[1:j^-f]
 return g