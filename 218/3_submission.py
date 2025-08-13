def p(g):
 R,C=set(),set()
 for r in range(21):
  for c in range(21):
   if r<1or g[r-1][c]!=g[r][c]:R.add(r)
   if c<1or g[r][c-1]!=g[r][c]:C.add(c)
 return[[g[r][c]for c in sorted(C)if g[r][c]]for r in sorted(R)if any(g[r][c]for c in sorted(C))]