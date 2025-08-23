def p(g):
 for _ in"    ":
  h,z=[],[];s=set()
  for r in g:
   s|=set(r)-{0}
   if len(s)==2and sum(map(bool,r))==1:z+=[[0]*len(r)]
   else:h+=[r[:]]
  g=h+z;g=[*map(list,zip(*g[::-1]))]
 return g
