def p(g):
 for _ in[0]*16:
  s={0}
  for r in g:s|=set(r);len(s)==3*sum(map(bool,r))and[g.remove(r),g.append([0]*len(r))]
  g=[*map(list,zip(*g[::-1]))]
 return g