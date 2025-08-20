def p(g):
 h=len(g);w=len(g[0])
 s=lambda r,d:(w*[0]+r+w*[0])[w-d:][:w]
 for k in range(1,h+1):
  for d in range(-w,w+1):
   if g[k:]==[s(r,d)for r in g[:h-k]]:
    while len(g)<10:g+=s(g[-k],d),
    return g
