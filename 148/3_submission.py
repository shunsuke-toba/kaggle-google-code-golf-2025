def p(g):
 w=len(g[0])-1
 for a,b in zip((r for r in g if r[0]==2),(r for r in g if r[w]==2)):
  if 8 in a:j=a.index(8);a[j]=4;a[1:j]=[8]*~-j;b[:w]=[8]*w
  elif 8 in b:j=b.index(8);b[j]=4;b[j+1:w]=[8]*(w+~j);a[1:]=[8]*w
 return g
