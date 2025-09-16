def p(g):
 s=sum(g,[])
 for d in s:
  x,y=zip(*[divmod(i,len(g[0]))for i,v in enumerate(s)if v==d]);b=min(y);n=x[-1]-x[0]
  if n<18>max(y)-b:m=-~n//3;return[[sum({*s},-d)*(v==d)for v in r[b::m][:3]]for r in g[x[0]::m][:3]]