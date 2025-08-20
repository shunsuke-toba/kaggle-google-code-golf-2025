def p(g):
 h=len(g);w=len(g[0]);s={*sum(g,[])}-{0};d=1,0,-1,0,1;R=range(4)
 for b in s:
  if sum(r.count(b)for r in g)<2:continue
  for a in s-{b}:
   v=[[0]*w for _ in g]
   for y in range(h):
    for x in range(w):
     if v[y][x]or g[y][x]not in(a,b):continue
     q=[y,x];v[y][x]=1;A=[];B=0
     while q:
      X=q.pop();Y=q.pop()
      if g[Y][X]==a:A+=Y,X
      else:B+=1;ay,ax=Y,X
      for i in R:
       ny,nx=Y+d[i],X+d[i+1]
       if h>ny>=0<=nx<w and g[ny][nx]in(a,b)and not v[ny][nx]:v[ny][nx]=1;q+=ny,nx
     if B and B<2<len(A):
      F=[(A[i]-ay,A[i+1]-ax)for i in range(0,len(A),2)];break
    else:continue
    break
   else:continue
   break
  else:continue
  break
 else:return g
 o=[r[:]for r in g];v=[[0]*w for _ in g]
 for y in range(h):
  for x in range(w):
   if g[y][x]==b and not v[y][x]:
    q=[y,x];v[y][x]=1;c=[];l=m=9**9;r=u=-l
    while q:
     X=q.pop();Y=q.pop();c+=[(Y,X)];l=min(l,X);r=max(r,X);m=min(m,Y);u=max(u,Y)
     for i in R:
      ny,nx=Y+d[i],X+d[i+1]
      if h>ny>=0<=nx<w and g[ny][nx]==b and not v[ny][nx]:v[ny][nx]=1;q+=ny,nx
    n=max(u-m+1,r-l+1);C=a
    for Y,X in c:
     for i in R:
      ny,nx=Y+d[i],X+d[i+1]
      if h>ny>=0<=nx<w:
       t=g[ny][nx]
       if t not in(0,b):C=t;break
     else:continue
     break
    for dy,dx in F:
     sy=m+dy*n;sx=l+dx*n
     for Y in range(sy,sy+n):
      for X in range(sx,sx+n):
       if h>Y>=0<=X<w:o[Y][X]=C
 return o
