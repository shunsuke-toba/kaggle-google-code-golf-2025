def p(g):
 h=bytes(sum(g,[]));s=j=13;a,b=divmod(h.find(4),13);c,d=divmod(h.rfind(4),13);o=[r[b:d+1]for r in g[a:c+1]]
 for r,v in enumerate(h):
  r,k=divmod(r,13)
  if r-a|c-r|k-b|d-k<0<v!=4:
   if r<s:s=r
   if k<j:j=k;f=v!=o[1][0]
 for r in o[1:c-a]:
  s+=1;r[1:-1]=g[s-1][j:j+d-b-1][::1-2*f]
 return o