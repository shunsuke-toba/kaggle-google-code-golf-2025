def p(g):
 f=sum(g,[]);w=len(g[0])
 for v in {*f}-{0}:
  i=f.index(v);j=f.index(v,-~i);a=i//w;b=j//w;c,d=sorted((i%w,j%w))
  for R in g[a:b+1]:R[c:d+1]=[v]*-~(d-c)
 return g
