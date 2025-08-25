def p(g):
 r=range;S=sum
 for L in r(3,7):
  for y in r(12):
   M=g[y:y+L];I=M[1:-1]
   for x in r(12):
    if 20*~-L==S(S(m[x:x+L])for m in M)>S(S(m[x+1:x+L-1])for m in I)<1:
     for m in I:m[x+1:x+L-1]=[2]*(L-2)
 return g
