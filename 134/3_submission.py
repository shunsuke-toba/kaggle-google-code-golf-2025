def p(g):
 s=sum(g,[]);w=len(g[0])
 for d in s:
  x,y=zip(*[(i//w,i%w)for i,v in enumerate(s)if v==d]);a=x[0];b=min(y);n=x[-1]-a
  if n==max(y)-b<18:m=-~n//3;t=0,1,2;return[[sum({*s},-d)*(g[a+i*m][b+j*m]==d)for j in t]for i in t]