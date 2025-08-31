def p(g):
 f=sum(g,[]);r=range;a,x=divmod(f.index(k:=min(f,key=f.count)),21);h=f[x::21].count(k);w=g[a].count(k)
 for i in r(22-h):
  for j in r(22-w):
   if max(sum(R[j+1:j+w-1])for R in g[i+1:i+h-1])<1:
    for k in r(h):g[i+k][j:j+w]=g[a+k][x:x+w]
 return g