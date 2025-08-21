def p(g):
 for _ in 0,1:
  for R in g:
   for c in{*R}-{0}:
    try:a=R.index(c);b=len(R)-R[::-1].index(c);R[a:b]=[c]*(b-a)
    except:0
  g=[*map(list,zip(*g))]
 return g
