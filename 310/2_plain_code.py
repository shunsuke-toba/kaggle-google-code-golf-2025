def p(g):
  h,w=len(g),len(g[0])
  box={}
  for i,row in enumerate(g):
    for j,v in enumerate(row):
      if v==0: continue
      b=box.get(v)
      if b is None: box[v]=[i,i,j,j]
      else:
        if i<b[0]: b[0]=i
        if i>b[1]: b[1]=i
        if j<b[2]: b[2]=j
        if j>b[3]: b[3]=j

  def ok(v,r0,r1,c0,c1):
    if r1<=r0 or c1<=c0: return False
    if any(g[r0][j]!=v or g[r1][j]!=v for j in range(c0,c1+1)): return False
    if any(g[i][c0]!=v or g[i][c1]!=v for i in range(r0,r1+1)): return False
    for i in range(r0+1,r1):
      if v in g[i][c0+1:c1]: return False
    return True

  best=None; best_key=None
  for v,(r0,r1,c0,c1) in box.items():
    if not ok(v,r0,r1,c0,c1): continue
    H,W=r1-r0+1,c1-c0+1
    key=(max(H,W), H*W, v)  # 指定の基準＋安定化のためのタイブレーク
    if best_key is None or key<best_key:
      best_key=key; best=(r0,r1,c0,c1)

  r0,r1,c0,c1=best
  return [row[c0:c1+1] for row in g[r0:r1+1]]