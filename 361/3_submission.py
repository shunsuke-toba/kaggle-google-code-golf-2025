def p(g):
 z=[(i+j*1j,v)for i,r in enumerate(g)for j,v in enumerate(r)if v];d={}
 for a,w in z:
  for b,v in z:
   if w==v and a-b:t=(a+b*1j)/(1+1j);d[t]=d.get(t,0)+1
 p=max(d,key=d.get)
 for s,v in z:
  for _ in"1234":g[int(s.real)][int(s.imag)]=v;s=(s-p)*1j+p
 return g
