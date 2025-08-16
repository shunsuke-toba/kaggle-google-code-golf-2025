def p(g,R=range):
 d={}
 for y in R(10):
  for x in R(10):
   v=g[y][x]
   if v:
    try:a,b=d[v];s=1-2*(y<a);t=1-2*(x<b);[g[a+i*s].__setitem__(b+i*t,v)for i in R((y-a)*s+1)]
    except:d[v]=(y,x)
 return g
