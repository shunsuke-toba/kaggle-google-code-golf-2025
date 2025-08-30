def p(g):
 s={*sum(g,[])};E=enumerate
 for d in s:
  x,y=zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v==d]);a=min(x);b=min(y);n=max(x)-a
  if n==max(y)-b<18:m=-~n//3;t=0,1,2;return[[(sum(s)-d)*(g[a+i*m][b+j*m]==d)for j in t]for i in t]