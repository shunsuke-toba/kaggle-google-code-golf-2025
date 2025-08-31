def p(g):
 f=sum(g,[]);r=range;a=f.index(k:=min(f,key=f.count));x=a%21;h=f[a::21].count(k);a//=21;w=g[a].count(k)
 for i in r(22-h):
  for j in r(22-w):
   if max(sum(R[j+1:j+w-1])for R in g[i+1:i+h-1])<1:
    for k in r(h):g[i+k][j:j+w]=g[a+k][x:x+w]
 return g