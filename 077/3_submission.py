def p(g):
 e=enumerate;s={(i,j)for i,r in e(g)for j,v in e(r)if v==2}
 while s:
  t={s.pop()};a=c=99;b=d=0
  while t:y,x=t.pop();a=min(a,y);b=max(b,y);c=min(c,x);d=max(d,x);t|=s&{(y+i//5-2,x+i%5-2)for i in range(25)};s-=t
  for r in g[a:b+1]:r[c:d+1]=[4>>(x==2)for x in r[c:d+1]]
 return g
