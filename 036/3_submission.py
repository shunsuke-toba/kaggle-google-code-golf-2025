def p(g):
 h,w=len(g),len(g[0]);s={v for r in g for v in r if v}
 for c in s:
  v=[[0]*w for _ in range(h)];n=0;r=[]
  def d(y,x,a,b,e,f):
   if-1<y<h and-1<x<w and not v[y][x]and g[y][x]==c:
    v[y][x]=1;a=min(a,y);b=max(b,y);e=min(e,x);f=max(f,x)
    for i,j in((0,1),(0,-1),(1,0),(-1,0)):a,b,e,f=d(y+i,x+j,a,b,e,f)
   return a,b,e,f
  for y in range(h):
   for x in range(w):
    if g[y][x]==c and not v[y][x]:a,b,e,f=d(y,x,y,y,x,x);r+=(a,b,e,f),;n+=1
  if n==1:a,b,e,f=r[0];return[g[y][e:f+1]for y in range(a,b+1)]
 return g
