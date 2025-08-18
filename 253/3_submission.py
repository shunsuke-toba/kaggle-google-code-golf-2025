def p(g):
 o=[0]*16
 for r,s in zip(g,g[1:]):
  for w in zip(r,r[1:],s,s[1:]):
   if w.count(max(w))==3:
    i=w.index(0);k=(10,8,2,0)[i]
    o[k],o[k+1],o[k+4],o[k+5]=w
 return[o[:4],o[4:8],o[8:12],o[12:]]
