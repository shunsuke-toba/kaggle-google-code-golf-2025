def p(g):
 k=[0]*4
 for g,h in zip(g,g[1:]):
  for w in zip(g,g[1:],h,h[1:]):
   k[w.index(0)]+=max(w)*(w.count(0)<2)
 a,b,c,d=k;return((d,d,c,c),(d,0,0,c),(b,0,0,a),(b,b,a,a))
