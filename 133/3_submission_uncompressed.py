def p(g):
 i=len(g);w=len(g[0])
 def l(t,x):
  h=[(t,x,g[t][x])];g[t][x]=0
  for t,x in(t+1,x),(t,x+1),(t-1,x),(t,x-1):
   if w>x>-1<t<i>g[t][x]>0:h+=l(t,x)
  return h
 i=[l(t,x)for t in range(i)for x in range(w)if g[t][x]]
 d=min((len(i)<3,len(i),i)for i in i)[2];r,c,o=min((sum(v==i[2]for t,x,v in d),i)for i in d)[1]
 for i in i:
  h=[(t,x)for t,x,v in i if v==o]
  for t,x,v in d:
   for j,p in h:g[(t-r)*int(len(h)**.5)+j][(x-c)*int(len(h)**.5)+p]=(min(v for t,x,v in i if v^o),o)[v==o]
 return g