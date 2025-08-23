def p(g):
 f=sum(g,[]);k=min({*f}-{0},key=f.count);R=range
 a=f.index(k);b=441+~f[::-1].index(k);d=b-a;H=d//21+1;W=d%21+1;u,l=divmod(a,21)
 for y in R(22-H):
  for x in R(22-W):
   if(x-l|y-u)and not sum(sum(r[x+1:x+W-1])for r in g[y+1:y+H-1]):
    for t in R(H):g[y+t][x:x+W]=g[u+t][l:l+W]
    return g
