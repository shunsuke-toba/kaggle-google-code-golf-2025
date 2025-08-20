def p(g,F=filter):
 for c in{*sum(g,[])}:
  f=lambda r:r.count(c)
  h=[*map(list,zip(*F(f,zip(*list(F(f,g))))))]
  if sum(h,[]).count(c)==len(h)*len(h[0]):e=c
 for r in g:
  if r.count(e)or sum(r)<1:continue
  M=min(z:=[i for i,x in enumerate(r)if x>0])+max(z)
 for z in range(256):
  x,y=z//16,z%16
  if 0<=M-y<16and (c:=g[x][y])!=e:g[x][M-y]=c
 return g