def p(g):
 r=range;S=sum
 for L in r(3,7):
  for y in(R:=r(13-L)):
   M=g[y:y+L]
   for x in R:
    if S(S(m[x:x+L])for m in M)==20*~-L and S(S(m[x+1:x+L-1])for m in M[1:-1])<1:
     for m in M[1:-1]:m[x+1:x+L-1]=[2]*(L-2)
 return g
