def p(g):
 f=sum(g,[]);w=len(g[0]);s=sorted
 for v in {*f}-{0}:
  i=f.index(v);j=f.index(v,-~i);a,b=s((i//w,j//w));c,d=s((i%w,j%w))
  for R in g[a:b+1]:R[c:d+1]=[v]*-~(d-c)
 return g
