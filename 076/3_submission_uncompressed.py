def p(g):
 h=len(g);w=len(g[0]);s=[divmod(sum(g,[]).index(3),w)]
 for y,x in s:s+=[(a,b)for a in range(y-1,y+2)for b in range(x-1,x+2)if h>a>-1<b<w>g[a][b]>((a,b)in s)<1]
 r,c=zip(*s);t=[r[min(c):max(c)+1]for r in g[min(r):max(r)+1]]
 for i in range(8):
  for y in range(h-len(t)+1):
   for x in range(w-len(t[0])+1):
    if all(t[a][b]&1or g[y+a][x+b]==t[a][b]for a in range(len(t))for b in range(len(t[0]))):
     for a in range(len(t)):g[y+a][x:x+len(t[0])]=t[a]
  t=[*zip(*t[::-1])]
  if i==3:t=t[::-1]
 return g