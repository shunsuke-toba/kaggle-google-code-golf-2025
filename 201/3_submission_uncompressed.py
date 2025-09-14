def p(g):
 j=s=w=13;h=bytes(sum(g,[]));a,b=divmod(h.find(4),w);c,d=divmod(h.rfind(4),w);o=[r[b:-~d]for r in g[a:-~c]];t=o[1][0]
 for r,v in enumerate(h):k=r%w;r//=w;r-a|c-r|k-b|d-k<0<v&-5 and(s:=min(s,r),k<j and(j:=k,f:=v!=t))
 for r in o[1:-1]:r[1:-1]=g.pop(s)[j:j+~b+d][::1-2*f]
 return o
