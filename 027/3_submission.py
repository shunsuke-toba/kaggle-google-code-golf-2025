def p(g):
 h=len(g);w=len(g[0])
 B=A=None
 for y,x in ((9,9),(10,10)):
  s=set();m=0;ok=1
  for r in range(h):
   for c in range(w):
    if g[r][c]==1:
     rr=y-r;cc=x-c
     if rr<0 or rr>=h or cc<0 or cc>=w:ok=0;break
     if g[rr][cc]==0:
      if cc*2<=x:s.add((rr,cc))
      else:m+=1
   if not ok:break
  if ok:
   t=(m,len(s),-y,-x)
   if B is None or t<B:B=t;A=s
 o=[r[:] for r in g]
 if A:
  for r,c in A:o[r][c]=2
 return o

