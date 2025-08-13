def p(g):
 h,w=len(g),len(g[0]);R=[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]
 if not R:return g
 P={c:c for c in R}
 def F(x):
  if P[x]!=x:P[x]=F(P[x])
  return P[x]
 for i,r in enumerate(R):
  for s in R[i+1:]:
   if max(abs(s[0]-r[0]),abs(s[1]-r[1]))<=2:x,y=F(r),F(s);x!=y and exec("P[x]=y")
 C={}
 for c in R:r=F(c);C[r]=C.get(r,[])+[c]
 o=[r[:]for r in g]
 for v in C.values():
  a=min(c[0]for c in v);b=max(c[0]for c in v);c=min(c[1]for c in v);d=max(c[1]for c in v)
  for i in range(a,-~b):
   for j in range(c,-~d):o[i][j]!=2 and exec("o[i][j]=4")
 return o
