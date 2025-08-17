def p(g):
 h=len(g);w=len(g[0]);B=max(f:=sum(g,[]),key=f.count);V=[[0]*w for _ in g];m={};T=0
 for k in range(h*w):
  r,c=divmod(k,w)
  if g[r][c]!=B and not V[r][c]:
   S=[(r,c)];V[r][c]=1;A=[];C=set();a=b=r;e=f=c
   while S:
    r,c=S.pop();A+=(r,c),;C|={g[r][c]}
    a=min(a,r);b=max(b,r);e=min(e,c);f=max(f,c)
    for i in-1,0,1:
     for j in-1,0,1:
      if i|j and h>(x:=r+i)>=0<= (y:=c+j)<w and g[x][y]!=B and not V[x][y]:V[x][y]=1;S+=(x,y),
   len(C)>2 and(T:=A)
   len(C)<2 and (s:=b-a+1)==f-e+1 and m.setdefault(*C,[]).append((a,e,s))
 A=T
 L=[g[r][c]for r,c in A];b=max(L,key=L.count);p,q=set(L)-{b}
 for r,c in A:col=g[r][c];col==p and(pa:=(r,c));col==q and(pc:=(r,c))
 R=pc[0]-pa[0];C=pc[1]-pa[1];S=[(r-pa[0],c-pa[1])for r,c in A if g[r][c]==b];o=[r[:]for r in g]
 for ar,ac,s in m[p]:
  for br,bc,t in m[q]:
   if s==t:
    dr=br-ar;dc=bc-ac
    for u in 0,1:
     for v in-1,1:
      for w in-1,1:
       x,y=R*v,C*w
       if u:x,y=y,x
       if x and (k:=dr//x)>0 and dr%x==0 and y*k==dc or y and (k:=dc//y)>0 and dc%y==0 and x*k==dr:
        for r,c in S:
         r*=v;c*=w
         if u:r,c=c,r
         rr=ar+r*k;cc=ac+c*k
         for i in range(k):o[rr+i][cc:cc+k]=[b]*k
 return o
