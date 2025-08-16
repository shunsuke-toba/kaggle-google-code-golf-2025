def p(g,R=range):
 h,w=len(g),len(g[0])
 A,B=[],[[0]*w for _ in R(h)]
 for r in R(h):A.append([sorted(g[r])[w//2]]*w)
 for c in R(w):
  m=sorted([g[r][c]for r in R(h)])[h//2]
  for r in R(h):B[r][c]=m
 S=lambda x:sum(g[r][c]==x[r][c]for r in R(h)for c in R(w))
 return[B,A][S(A)>=S(B)]