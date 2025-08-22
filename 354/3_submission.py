def p(g):
 T=range(10)
 def d(r,s,w):
  if-1<r<10>s>-1<5==g[r][s]:g[r][s]=w;d(r+1,s,w);d(r-1,s,w);d(r,s+1,w);d(r,s-1,w)
 [d(r,s,g[0][s])for s in T if g[0][s]for r in T if g[r][s]==5]
 return g
