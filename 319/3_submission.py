def p(g,R=range):
 h=len(g);w=len(g[0]);A=[99]*10;B=[99]*10;C=[-1]*10;D=[-1]*10;E=[0]*10
 for i in R(h):
  for j in R(w):
   c=g[i][j];E[c]+=1;A[c]=min(A[c],i);C[c]=max(C[c],i);B[c]=min(B[c],j);D[c]=max(D[c],j)
 b=E.index(max(E));T=R(1,10)
 for c in T:
  if c==b or C[c]<A[c]:continue
  H=C[c]-A[c]+1;W=D[c]-B[c]+1;x=y=1
  for ph in R(-(H%2),1):
   for pw in R(-(W%2),1):
    ok=1
    for i in R((H+1)//2):
     for j in R((W+1)//2):
      u=A[c]+i*2+ph;v=B[c]+j*2+pw
      p=sum(0<=s<h and 0<=t<w and g[s][t]==c for s in(u,u+1)for t in(v,v+1))
      s=sum(not(0<=s<h and 0<=t<w)for s in(u,u+1)for t in(v,v+1))
      if p and p+s!=4:ok=0
    if ok:x=ph;y=pw
  if x==1:continue
  x-=A[c]%2;y-=B[c]%2
  th=(h-x+1)//2;tw=(w-y+1)//2
  t=[[any(0<=s<h and 0<=t0<w and g[s][t0]==c for s in(i*2+x,i*2+x+1)for t0 in(j*2+y,j*2+y+1))for j in R(tw)]for i in R(th)]
  for k in T:
   if k in (c,b) or C[k]<A[k]:continue
   for u in R(-h,h):
    for v in R(-w,w):
     if all(((0<=u+i<h and 0<=v+j<w and g[u+i][v+j]==k)==t[i][j])for i in R(th)for j in R(tw)):
      return [[(g[i][j]==k)*k or b for j in R(B[k],D[k]+1)]for i in R(A[k],C[k]+1)]