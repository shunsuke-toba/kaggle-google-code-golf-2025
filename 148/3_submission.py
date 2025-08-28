def p(g):
 for a,b in zip(*[[r for r in g if r[i]]for i in(0,-1)]):
  c=[8]*~-len(a)
  if 8in a:j=a.index(8);a[1:j+1]=[8]*~-j+[4];b[:-1]=c
  elif 8in b:j=b.index(8);b[j:-1]=[4]+c[j+1:];a[1:]=c
 return g