def p(g):
 h=len(g);w=len(g[0]);B=max(f:=sum(g,[]),key=f.count);V=[[0]*w for _ in g];d={};T=0
 for k in range(h*w):
  r,c=divmod(k,w)
  if g[r][c]!=B and not V[r][c]:
   S=[(r,c)];V[r][c]=1;A=[];C=set()
   while S:
    r,c=S.pop();A+=(r,c),;C|={g[r][c]}
    for i in-1,0,1:
     for j in-1,0,1:
      if i|j and h>(x:=r+i)>=0<= (y:=c+j)<w and g[x][y]!=B and not V[x][y]:V[x][y]=1;S+=(x,y),
   len(C)==3 and(T:=(A,C))
   len(C)==1 and d.setdefault(*C,[]).append(A)
 A,C=T
 q=[g[r][c]for r,c in A];b=max(q,key=q.count);a,c=[x for x in C if x!=b]
 for p0 in A:col=g[p0[0]][p0[1]];col==a and(pa:=p0);col==c and(pc:=p0)
 R=pc[0]-pa[0];C=pc[1]-pa[1];Bs=[(r-pa[0],c-pa[1])for r,c in A if g[r][c]==b];o=[r[:]for r in g]
 for A in d[a]:
  r,e=zip(*A);ar=min(r);ac=min(e);s=max(r)-ar+1
  if max(e)-ac+1==s:
   for A2 in d[c]:
    r2,e2=zip(*A2);br=min(r2);bc=min(e2)
    if max(r2)-br+1==s and max(e2)-bc+1==s:
     dr=br-ar;dc=bc-ac
     for u in 0,1:
      for v in-1,1:
       for w in-1,1:
        dx,dy=R,C
        if u:dx,dy=dy,dx
        dx*=v;dy*=w
        if dx and dr%dx==0 and dy*(k:=dr//dx)==dc and k>0 or dy and dc%dy==0 and dx*(k:=dc//dy)==dr and k>0:
         for rb,cb in Bs:
          if u:rb,cb=cb,rb
          rb*=v;cb*=w
          for i in range(k):
           for j in range(k):o[ar+rb*k+i][ac+cb*k+j]=b
 return o
