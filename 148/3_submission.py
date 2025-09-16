def p(g):
 for a,b in zip(*[[r for r in g if r[i]]for i in(0,-1)]):
  if (f:=8in b):a,b=b,a
  if 8in a:c=[8]*~-len(a);j=a.index(8);b[f:]=c+[2]*(1-f);a[j]=4;a[f*j+1:-f or j]=c[1^f:~j*f or j]
 return g