def p(g):
 g=sum(g,[]);r=[0]*225
 for t in 7,3:
  r[p:=g.index(7//t)]=7//t
  while t in g:j=g.index(t);r[p+(k:=j-p)//(abs(k)//15 or abs(k))]=t;g[j]=0
 return[*zip(*[iter(r)]*15)]
