def p(g):
 h=len(g);w=len(g[0])
 s=lambda r,d:[0 if j-d<0 or j-d>=w else r[j-d]for j in range(w)]
 for k in range(1,h+1):
  for d in range(-w,w+1):
   if all(s(g[i-k],d)==g[i]for i in range(k,h)):
    while len(g)<10:g.append(s(g[-k],d))
    return g
