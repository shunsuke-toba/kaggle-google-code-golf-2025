def p(g):
 for d in(s:=sum(g,[])):
  (a,*_,c),y=zip(*(divmod(i,len(g[0]))for i,v in enumerate(s)if v==d));b=min(y);c-=a-1
  if max(y)-b<c<19:c//=3;return[[sum({*s},-d)*(v==d)for v in r[b::c][:3]]for r in g[a::c][:3]]