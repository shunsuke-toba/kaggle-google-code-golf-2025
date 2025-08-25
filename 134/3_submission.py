def p(g):
 s={*sum(g,[])}-{0}
 for d in s:
  x,y=zip(*{(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==d});a=min(x);b=min(y);n=max(x)-a+1
  if 19>n==max(y)-b+1:t=0,1,2;return[[(sum(s)-d)*(g[a+i*n//3][b+j*n//3]==d)for j in t]for i in t]
