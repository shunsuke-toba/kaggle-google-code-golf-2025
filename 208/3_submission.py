def p(g):
 k=min(f:=sum(g,[]),key=f.count);a=f.index(k);y,x=divmod(a,21);h,w=divmod(462-f[::-1].index(k)-a,21);R=range
 for i in R(22-h):
  for j in R(22-w):
   if(j-x|i-y)and sum(sum(r[j+1:j+w-1])for r in g[i+1:i+h-1])<1:
    for t in R(h):g[i+t][j:j+w]=g[y+t][x:x+w]
    return g