def p(g):
 f=sum(g,[]);k=min(f,key=f.count);u,l=divmod(a:=f.index(k),21);d=440-f[::-1].index(k)-a;H=d//21+1;W=d%21+1;R=range
 for y in R(22-H):
  for x in R(22-W):
   if(x-l|y-u)and not sum(sum(r[x+1:x+W-1])for r in g[y+1:y+H-1]):
    for t in R(H):g[y+t][x:x+W]=g[u+t][l:l+W]
    return g
