def p(g):
 g=sum(g,[]);r=[0]*225
 for t in 7,3:
  r[p:=g.index(7//t)]=7//t
  for j in range(225):
   if g[j]==t:r[p+(k:=j-p)//(abs(k)//15 or abs(k))]=t
 return[*zip(*[iter(r)]*15)]
