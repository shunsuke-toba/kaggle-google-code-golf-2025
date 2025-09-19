def p(g):
 k=[0]*4
 p,*g=g
 for q in g:
  for w in zip(p,q,p[1:],q[1:]):k[w.index(0)]|=sorted(w)[1];p=q
 d,b,c,a=k;return(a,a,b,b),(a,0,0,b),(c,0,0,d),(c,c,d,d)