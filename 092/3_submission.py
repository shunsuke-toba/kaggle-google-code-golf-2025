def p(g):
 for _ in 0,1:
  for R in g:
   A=R[:]
   for c in{*A}-{0}:
    a=A.index(c);b=len(A)-A[::-1].index(c)-1
    if a<b:R[a:b+1]=[c]*(b-a+1)
  g=[*map(list,zip(*g))]
 return g
