def p(g):
 h=len(g);w=len(g[0]);B=max(f:=sum(g,[]),key=f.count);V=[[0]*w for _ in g];m={};T=0
 for k in range(h*w):
  r,c=divmod(k,w)
  if g[r][c]!=B and not V[r][c]:
   S=[(r,c)];V[r][c]=1;A=[];C=set();a=b=r;e=f=c
   while S:
    r,c=S.pop();A+=(r,c),;C|={g[r][c]}
    a=min(a,r);b=max(b,r);e=min(e,c);f=max(f,c)
    for q in range(9):
     if q-4and h>(x:=r+q//3-1)>-1<(y:=c+q%3-1)<w>g[x][y]!=B>0==V[x][y]:V[x][y]=1;S+=(x,y),
   if len(C)>2:T=A
   if len(C)<2and(s:=b-a+1)==f-e+1:m.setdefault(*C,[]).append((a,e,s))
 A=T;L=[g[r][c]for r,c in A];b=max(L,key=L.count);p,q=set(L)-{b}
 for r,c in A:l=g[r][c];l==p and(z:=(r,c));l==q and(d:=(r,c))
 R=d[0]-z[0];C=d[1]-z[1];S=[(r-z[0],c-z[1])for r,c in A if g[r][c]==b];g=[r[:]for r in g]
 for o,n,s,v,u,w,r,c in[(o,n,s,v,u,w,r,c)for o,n,s in m[p]for v,u,t in m[q]for w in range(8)for r,c in S if s==t]:
  j,k,l=w//4,w//2%2*2-1,w%2*2-1;E,F=v-o,u-n;x,y=R*k,C*l
  if j:x,y=y,x
  if x and(I:=E//x)>0==E%x<(y*I==F)or y and(I:=F//y)>0==F%y<(x*I==E):
   r*=k;c*=l
   if j:r,c=c,r
   J,K=o+r*I,n+c*I
   for i in range(I):g[J+i][K:K+I]=[b]*I
 return g