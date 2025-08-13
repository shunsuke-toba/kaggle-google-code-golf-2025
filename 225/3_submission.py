def p(g):
 N,M,d=len(g),len(g[0]),(1,-1,-1,1,1)
 for r in range(N-1):
  for c in range(M-1):
   if g[r][c]!=g[r][c+1]and g[r][c]!=g[r+1][c]and g[r][c]!=g[r+1][c+1]:
    for i in range(4):
     nr,nc=int(r+.7+d[i]*.5),int(c+.7+d[i+1]*.5)
     for x in range(2):
      for y in range(2):
       nnr,nnc=int(r+.7-d[i]*(1.5+x)),int(c+.7-d[i+1]*(1.5+y))
       if 0<=nnr<N and 0<=nnc<M:g[nnr][nnc]=g[nr][nc]
    return g