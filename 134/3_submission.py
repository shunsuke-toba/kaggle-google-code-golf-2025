def p(g):
 for d in(s:=sum(g,[])):
  (a,*_,c),y=zip(*(divmod(i,len(g[0]))for i,v in enumerate(s)if v==d));k=len({*_})
  if k>c-a<18:return[[sum({*s},-d)*(v==d)for v in r[min(y)::k//3][:3]]for r in g[a:a+k:k//3]]