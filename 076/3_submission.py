def p(g):
 L=len;R=range;E=enumerate;h=L(g);S=[divmod(next(i for i,v in E(sum(g,[]))if v&1),w:=L(g[0]))]
 for y,x in S:S+=[(Y,X)for Y in R(y-1,y+2)for X in R(x-1,x+2)if h>Y>-1<X<w and g[Y][X]and(Y,X)not in S]
 r,c=zip(*S);t=[row[min(c):max(c)+1]for row in g[min(r):max(r)+1]]
 for i in R(8):
  for y in R(h-L(t)+1):
   for x in R(w-L(t[0])+1):
    if all(g[y+a][x+b]==u for a,r in E(t)for b,u in E(r)if u&1<1<u):
     for a,r in E(t):
      for b,u in E(r):g[y+a][x+b]|=u
  t=[*zip(*t[::-1])];i-3 or t.reverse()
 return g
