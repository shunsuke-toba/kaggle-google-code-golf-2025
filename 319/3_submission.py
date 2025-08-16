def p(g,R=range):
 L=len;h=L(g);w=L(g[0]);n=10;a=[99]*n;b=[99]*n;c=[-1]*n;d=[-1]*n;e=[0]*n
 for y in R(h):
  for z in R(w):x=g[y][z];e[x]+=1;a[x]=min(a[x],y);c[x]=max(c[x],y);b[x]=min(b[x],z);d[x]=max(d[x],z)
 m=e.index(max(e));r=R(1,n)
 for x in r:
  if x==m or c[x]<a[x]:continue
  y=z=2
  for p in R(-((c[x]-a[x]+1)&1),1):
   for q in R(-((d[x]-b[x]+1)&1),1):
    if all((P:=sum(0<=s<h and 0<=t<w and g[s][t]==x for s in(u,u+1)for t in(v,v+1)))<1 or P==sum((0<=s<h)*(0<=t<w)for s in(u,u+1)for t in(v,v+1))for u in R(a[x]+p,c[x]+p+1,2)for v in R(b[x]+q,d[x]+q+1,2)):y=p;z=q
  if y>1:continue
  y-=a[x]&1;z-=b[x]&1
  t=[[any(0<=s<h and 0<=t<w and g[s][t]==x for s in(i,i+1)for t in(j,j+1))for j in R(z,w,2)]for i in R(y,h,2)]
  for k in r:
   if k in{x,m}or c[k]<a[k]:continue
   for u in R(-h,h):
    for v in R(-w,w):
     if all((0<=u+i<h and 0<=v+j<w and g[u+i][v+j]==k)==t[i][j]for i in R(L(t))for j in R(L(t[0]))):
      return [[k*(g[i][j]==k)or m for j in R(b[k],d[k]+1)]for i in R(a[k],c[k]+1)]
