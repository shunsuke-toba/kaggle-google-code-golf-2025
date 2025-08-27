def p(g,E=enumerate):
 z=[(i+j*1j,v)for i,r in E(g)for j,v in E(r)if v];p=max(t:=[(a+b*1j)/(1+1j)for a,w in z for b,v in z if w==v and a-b],key=t.count)
 for s,v in z:exec('g[int(s.real)][int(s.imag)]=v;s=(s-p)*1j+p;'*4)
 return g