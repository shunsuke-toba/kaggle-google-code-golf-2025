def p(g):
 R,C=len(g),len(g[0]);o=[r[:]for r in g];m=[];v=0
 for b in range(R*C):
  r,c=b//C,b%C
  if g[r][c]==5:m.append((r,c))
  elif g[r][c]>0:v=g[r][c]
 r1,r2=min(r for r,c in m)+1,max(r for r,c in m)-1
 c1,c2=min(c for r,c in m)+1,max(c for r,c in m)-1
 for c in range(c1,c2+1):
  if o[r1][c]<1:o[r1][c]=v
  if o[r2][c]<1:o[r2][c]=v
 for r in range(r1,r2+1):
  if o[r][c1]<1:o[r][c1]=v
  if o[r][c2]<1:o[r][c2]=v
 return o