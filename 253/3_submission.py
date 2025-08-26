def p(g):
 k=[0]*4
 for g,h in zip(g,g[1:]):
  for w in zip(g,h,g[1:],h[1:]):k[w.index(0)]|=sorted(w)[1]
 d,b,c,a=k;return(a,a,b,b),(a,0,0,b),(c,0,0,d),(c,c,d,d)
