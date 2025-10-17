def p(p):
 s=len(p);l=len(p[0]);i=[divmod(sum(p,[]).index(3),l)]
 for o,e in i:i+=[(u,r)for u in range(o-1,o+2)for r in range(e-1,e+2)if s>u>-1<r<l>p[u][r]>((u,r)in i)<1]
 r,n=zip(*i);f=[r[min(n):max(n)+1]for r in p[min(r):max(r)+1]]
 for n in range(8):
  for o in range(s-len(f)+1):
   for e in range(l-len(f[0])+1):
    if all(f[u][r]&1or p[o+u][e+r]==f[u][r]for u in range(len(f))for r in range(len(f[0]))):
     for u in range(len(f)):p[o+u][e:e+len(f[0])]=f[u]
  f=[*zip(*f[::-1])]
  if n==3:f=f[::-1]
 return p