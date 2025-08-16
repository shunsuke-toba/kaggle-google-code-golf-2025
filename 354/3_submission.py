def p(j):
 c=[x[:]for x in j];T=range(10)
 def d(r,s,w):
  if-1<r<10>s>-1<5==c[r][s]:c[r][s]=w;[d(r+a,s+b,w)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]]
 [d(r,s,j[0][s])for s in T if j[0][s]for r in T if c[r][s]==5]
 return c