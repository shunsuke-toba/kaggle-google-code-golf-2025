def p(g):
 L=len;w=L(g[0]);e=enumerate;s=[divmod(sum(g,[]).index(3),w)]
 for y,x in s:s+=[(a,b)for a in range(y-1,y+2)for b in range(x-1,x+2)if L(g)>a>-1<b<w>g[a][b]>((a,b)in s)<1]
 r,c=zip(*s);t=[r[min(c):max(c)+1]for r in g[min(r):max(r)+1]]
 for i in range(8):
  for y in range(L(g)-L(t)+1):
   for x in range(w-L(t[0])+1):
    if all((g[y+a][x+b]==u)|u&1 for a,r in e(t)for b,u in e(r)):
     for a,r in e(t):g[y+a][x:x+L(r)]=r
  t=[*zip(*t[::-1])];i-3or t.reverse()
 return g