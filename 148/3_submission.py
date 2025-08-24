def p(g):
 for a,b in zip(*[[r for r in g if r[i]>1]for i in(0,-1)]):
  m=len(a)-1
  if 8in a:j=a.index(8);a[1:j+1]=[8]*~-j+[4];b[:m]=[8]*m
  elif 8in b:j=b.index(8);b[j:m]=[4]+[8]*(m+~j);a[1:]=[8]*m
 return g
