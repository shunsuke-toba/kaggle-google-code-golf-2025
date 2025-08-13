def p(g):
 def s(g,t,o,m):
  M=len(g[0]);p=[];z=1;h=0;c=0
  for r in range(len(g)):
   if all(x<1for x in g[r]):z=1
   elif z:p.append(r);z=0;c=1
   else:c+=1
   h=max(h,c)
  f=p[0]
  for b in range(1,len(p)):
   r=p[b]+o;d=0
   for i in range(M-t-1,-1,-1):
    if d:break
    a=0
    for j in range(h):
     for k in range(t):
      if i+k<M:a+=g[r+j][i+k]<<(k*h+j)
    if any(g[r+j][i+k]for j in range(h)for k in range(t,t+2)if i+k<M):continue
    for i2 in range(M-t):
     if m*i2!=m*i:continue
     a2=0
     for j2 in range(h):
      for k2 in range(t):
       if i2+k2<M:a2+=g[f+j2][i2+k2]<<(k2*h+j2)
     if a==a2:
      c1,c2=i2+t,i2+t+1
      if any(g[f+l][c1]-g[f+l][c1+2]for l in range(h)):continue
      for d in range(M-i-t):
       k=i+t+d
       for l in range(h):g[r+l][k]=g[f+l][(c1,c2)[d%2]]//8
      d=1;break
   if not d:return
  return g
 u=[r[:]for r in g]
 for t in[3,2]:
  for m in[1,0]:
   for o in[0,-1]:
    g=[r[:]for r in u];v=s(g,t,o,m)
    if v:return v