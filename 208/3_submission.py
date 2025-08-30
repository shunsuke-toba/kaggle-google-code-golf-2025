def p(g):
 f=sum(g,[]);a=f.index(k:=min(f,key=f.count));x=a%21;h=f[a::21].count(k);a//=21;w=g[a].count(k)
 for i in range(22-h):
  for j in range(22-w):
   if max(sum(r[j+1:j+w-1])for r in g[i+1:i+h-1])<1:
    for H in range(h):g[i+H][j:j+w]=g[a+H][x:x+w]
 return g