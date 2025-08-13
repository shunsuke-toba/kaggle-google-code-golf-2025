def p(g):
 h=len(g);w=len(g[0])
 # check if rows are uniform (ignoring 0)
 def U(a):
  s={x for x in a if x}
  return len(s)<=1
 rh=all(U(r) for r in g)
 cv=all(U(g[r][c] for r in range(h)) for c in range(w))
 H= rh and not cv or (rh==cv and sum(U(r) for r in g)>=sum(U(g[r][c] for r in range(h)) for c in range(w)))
 o=[r[:] for r in g]
 if H:
  rv=[next((x for x in r if x),0) for r in g]
  d={}
  for r in range(h):
   v=rv[r]
   if not v:continue
   for c in range(w):
    if g[r][c]==0:
     d.setdefault(v,set()).add(c)
  for v,S in d.items():
   for r in range(h):
    if rv[r]==v:
     for c in S:o[r][c]=0
 else:
  cvl=[]
  for c in range(w):
   v=0
   for r in range(h):
    if g[r][c]:v=g[r][c];break
   cvl.append(v)
  d={}
  for r in range(h):
   for c in range(w):
    if g[r][c]==0:
     v=cvl[c]
     if v:d.setdefault(v,set()).add(r)
  for v,S in d.items():
   for c in range(w):
    if cvl[c]==v:
     for r in S:o[r][c]=0
 return o

