def p(g):
 s=[divmod(sum(g,[]).index(3),len(g[0]))]
 for y,x in s:s+=[(Y,X)for Y in range(y-1,y+2)for X in range(x-1,x+2)if len(g)>Y>-1<X<len(g[0])>g[Y][X]>((Y,X)in s)<1];r,c=zip(*s);t=[r[min(c):max(c)+1]for r in g[min(r):max(r)+1]]
 for i in range(8):
  for y in range(len(g)-len(t)+1):
   for x in range(len(g[0])-len(t[0])+1):
    if all((g[y+a][x+b]==u)|u&1 for a,r in enumerate(t)for b,u in enumerate(r)):
     for a,r in enumerate(t):g[y+a][x:x+len(r)]=r
  t=[*zip(*t[::-1])];i-3or t.reverse()
 return g