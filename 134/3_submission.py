def p(g):
 s=sum(g,[]);t=0,1,2
 for d in s:
  x,y=zip(*[divmod(i,len(g[0]))for i,v in enumerate(s)if v==d]);b=min(y);n=x[-1]-x[0]
  if n==max(y)-b<18:m=-~n//3;return[[sum({*s},-d)*(g[x[0]+i*m][b+j*m]==d)for j in t]for i in t]