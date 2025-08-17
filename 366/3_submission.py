from collections import*
def p(g):
 h=len(g);w=len(g[0]);c=Counter();b=defaultdict(lambda:[h,w,0,0])
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   c[v]+=1;m=b[v];m[0]=min(m[0],i);m[1]=min(m[1],j);m[2]=max(m[2],i);m[3]=max(m[3],j)
 d,s,t=[*sorted(c,key=c.get,reverse=True)][:3];sx,sy,ex,ey=b[s];dx,dy,fx,fy=b[d]
 V=set();L=[]
 for i in range(sx,ex+1):
  for j in range(sy,ey+1):
   if (i,j)in V or g[i][j]in(s,t):continue
   q=[(i,j)];V.add((i,j));C=[]
   while q:
    x,y=q.pop();C+=[(x,y)]
    for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
     X+=x;Y+=y
     if sx<=X<=ex and sy<=Y<=ey and(X,Y)not in V and g[X][Y]!=s:V.add((X,Y));q+=[(X,Y)]
   L+=[C]
 L.sort(key=lambda C:-sum(g[x][y]!=t for x,y in C))
 R=lambda a:[list(r)for r in zip(*a[::-1])]
 for C in L:
  xs=[x for x,_ in C];ys=[y for _,y in C]
  a=[[t]*(max(ys)-min(ys)+1)for _ in range(max(xs)-min(xs)+1)]
  for x,y in C:a[x-min(xs)][y-min(ys)]=g[x][y]
  T=[a]
  for _ in'123':a=R(a);T+=[a]
  a=[r[::-1]for r in T[0]];T+=[a]
  for _ in'123':a=R(a);T+=[a]
  ok=0
  for tr in T:
   nb=[(i,j,v)for i,r in enumerate(tr)for j,v in enumerate(r)if v!=t]
   bg=[(i,j)for i,r in enumerate(tr)for j,v in enumerate(r)if v==t]
   H=len(tr);W=len(tr[0])
   for x in range(dx,fx-H+2):
    for y in range(dy,fy-W+2):
     if all(g[x+i][y+j]==v for i,j,v in nb)and all(g[x+i][y+j]==d for i,j in bg):
      for i,r in enumerate(tr):
       for j,v in enumerate(r):g[x+i][y+j]=v
      ok=1;break
    if ok:break
   if ok:break
 dx,dy,fx,fy=b[d]
 return[g[i][dy:fy+1]for i in range(dx,fx+1)]
