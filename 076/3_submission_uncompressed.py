def p(g):
 w=len(g[0]);s=[divmod(sum(g,[]).index(3),w)]
 for y,x in s:s+=[(a,b)for a in range(y-1,y+2)for b in range(x-1,x+2)if len(g)>a>-1<b<w>g[a][b]>((a,b)in s)<1]
 r,c=zip(*s);t=[r[min(c):max(c)+1]for r in g[min(r):max(r)+1]]
 for i in range(8):
  for y in range(len(g)-len(t)+1):
   for x in range(w-len(t[0])+1):
    if all(u&1 or g[y+a][x+b]==u for a,r in enumerate(t)for b,u in enumerate(r)):
     for a,r in enumerate(t):g[y+a][x:x+len(r)]=r
  t=[*zip(*t[::-1])];i-3or t.reverse()
 return g