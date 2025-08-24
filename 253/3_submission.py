def p(g):
 o=[0]*16
 for g,h in zip(g,g[1:]):
  for w in zip(g,g[1:],h,h[1:]):
   if w.count(0)<2:k=(10,8,2,0)[w.index(0)];o[k],o[k+1],o[k+4],o[k+5]=w
 return[*zip(*[iter(o)]*4)]
