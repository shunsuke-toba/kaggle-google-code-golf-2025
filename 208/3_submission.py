def p(g):
 f=sum(g,[]);k=min(f,key=f.count);a=f.index(k);y,x=divmod(a,21);H,W=divmod(462-f[::-1].index(k)-a,21);r=range
 for Y in r(22-H):
  for X in r(22-W):
   if(X-x|Y-y)and not sum(sum(z[X+1:X+W-1])for z in g[Y+1:Y+H-1]):
    for t in r(H):g[Y+t][X:X+W]=g[y+t][x:x+W]
    return g
