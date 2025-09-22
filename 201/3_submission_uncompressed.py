def p(g):
 s=j=w=13
 h=bytes(sum(g,[]))
 a,b=divmod(h.find(4),w)
 c,d=divmod(h.rfind(4),w)
 o=[r[b:d+1]for r in g[a:c+1]]
 for r,v in enumerate(h):
  r,k=divmod(r,w)
  if r-a|c-r|k-b|d-k<0<v!=4:
   if r<s:s=r
   if k<j:j=k;f=v!=o[1][0]
 for r in o[1:-1]:
  r[1:-1]=g.pop(s)[j:j+d-b-1][::1-2*f]
 return o