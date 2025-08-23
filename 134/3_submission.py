def p(g):
 s={*sum(g,[])}-{0}
 for d in s:
  x,y=zip(*{(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==d});a=min(x);b=min(y);n=max(x)-a+1
  if 5<n==max(y)-b+1<19>n%3==0:break
 m=n//3;t=0,1,2
 return[[(sum(s)-d)*(g[a+i*m][b+j*m]==d)for j in t]for i in t]
