def p(g):
 for d in(s:=sum(g,[])):
  (a,*_,c),y=zip(*[divmod(i,len(g[0]))for i,v in enumerate(s)if v==d]);b=min(y);n=c-a
  if n<18>max(y)-b:m=-~n//3;return[[sum({*s},-d)*(v==d)for v in r[b::m][:3]]for r in g[a::m][:3]]