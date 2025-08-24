def p(g):
 for a,b in zip(*[[r for r in g if r[i]==2]for i in(0,-1)]):
  m=len(a)-1
  if 8 in a:j=a.index(8);a[j]=4;a[1:j]=[8]*~-j;b[:m]=[8]*m
  elif 8 in b:j=b.index(8);b[j]=4;b[j+1:m]=[8]*(m+~j);a[1:]=[8]*m
 return g
