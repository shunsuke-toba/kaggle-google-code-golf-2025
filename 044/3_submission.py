def p(g):
 h,w=len(g),len(g[0]);v=[[0]*w for _ in[0]*h];A=[];B={}
 def D(i,j,c,a):
  if 0<=i<h and 0<=j<w and v[i][j]<1 and g[i][j]==c:v[i][j]=1;a+=(i,j),;[D(i+d[0],j+d[1],c,a)for d in[(0,1),(0,-1),(1,0),(-1,0)]]
 for i in range(h):
  for j in range(w):
   if v[i][j]<1:
    a=[];D(i,j,g[i][j],a)
    if a:
     if g[i][j]==0 and all(g[y+dy][x+dx]==5 for y,x in a for dy,dx in[(0,1),(0,-1),(1,0),(-1,0)]if 0<=y+dy<h and 0<=x+dx<w and(y+dy,x+dx)not in a):A+=a,
     elif g[i][j]not in[0,5]:B[g[i][j]]=B.get(g[i][j],[])+[a]
 C=[(c,b[0])for c,b in B.items()if len(b)==1];r=[r[:]for r in g]
 def S(b):y=min(p[0]for p in b);x=min(p[1]for p in b);return sorted((i-y,j-x)for i,j in b)
 for c,b in C:
  s=S(b)
  for a in A:
   if S(a)==s:
    for y,x in b:r[y][x]=0
    Y,X=min(p[0]for p in b),min(p[1]for p in b);y,x=min(p[0]for p in a),min(p[1]for p in a)
    for i,j in b:r[i-Y+y][j-X+x]=c
    break
 return r
