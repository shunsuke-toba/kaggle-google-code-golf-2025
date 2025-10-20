def p(f):
 g=23;a=bytes(sum(f,[]));h=a.find(1);c=a.rfind(1);d=[(*[f&4for f in f[h%g+1:c%g]],)for f in f[h//g+1:c//g]];print(d)
 for h in range(4):
  for h in range(g*g):
   c=h%g;h//=g
   [(*[f&4for f in f[c:c+len(d[0])]],)for f in f[h:h+len(d)]]in(d,d[::-1])and[exec('f[h]=1')for f in f[h-(h>0):h-~len(d)]for h in range(g)if-2<h-c<=len(d[0])>f[h]]
  d=[*zip(*d[::-1])]
 return f