def p(j,e=enumerate):
 o=[[0]*len(j[0])for _ in j]
 for v in {*sum(j,[])}-{0}:
  k=[(r,c)for r,R in e(j)for c,V in e(R)if V==v];w,l=map(max,zip(*k))
  for r,c in k:o[r][c+(r<w)*(c<l)]=v
 return o
