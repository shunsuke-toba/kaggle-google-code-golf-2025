def p(j):
 c=[x[:]for x in j]
 def d(r,s,w):
  if-1<r<10>s>-1and c[r][s]==5:c[r][s]=w;[d(r+a,s+b,w)for a,b in[(-1,0),(1,0),(0,-1),(0,1)]]
 [d(r,s,j[0][s])for s in range(10)if j[0][s]for r in range(1,10)if c[r][s]==5]
 return c