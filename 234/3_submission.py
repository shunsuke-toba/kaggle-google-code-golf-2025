def p(g):
 for _ in[0]*16:
  s={0}
  for r in g:s|={*r};len(s)==3*sum(map(bool,r))and(g.append([0]*len(r)),g.remove(r))
  g=[*zip(*g[::-1])]
 return g
