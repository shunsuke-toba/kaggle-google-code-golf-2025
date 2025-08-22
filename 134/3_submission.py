def p(g):
 s={v for r in g for v in r if v}
 for d in s:
  x,y=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==d])
  t=max(x)-min(x)+1
  if t==max(y)-min(y)+1>5<t<19 and t%3<1:break
 a=min(x);b=min(y);m=t//3;c=sum(s)-d
 return[[c*(g[a+i*m][b+j*m]==d)for j in range(3)]for i in range(3)]
