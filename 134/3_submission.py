def p(g):
 s={v for r in g for v in r if v}
 for d in s:
  x,y=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==d])
  t=max(x)-min(x)+1
  if t==max(y)-min(y)+1>5<t<19 and t%3<1:
   a=min(x);b=min(y);m=t//3;break
 c=sum(s)-d
 r=range
 return[[c*any(g[i][j]==d for i in r(a+R*m,a+R*m+m) for j in r(b+C*m,b+C*m+m))for C in r(3)]for R in r(3)]
