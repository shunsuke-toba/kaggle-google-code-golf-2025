def p(g):
 for d in(s:=sum(g,[])):
  (a,*_,c),y=zip(*(divmod(i,len(g[0]))for i,v in enumerate(s)if v==d));c-=a-1
  if len({*_})==c<19:return[[sum({*s},-d)*(v==d)for v in r[min(y)::c//3][:3]]for r in g[a:a+c:c//3]]