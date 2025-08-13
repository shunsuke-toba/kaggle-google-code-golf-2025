def p(g):
 h,w=len(g),len(g[0]);V=[[0]*w for _ in range(h)];C=[]
 def D(i,j,c,s):
  if i<0 or i>=h or j<0 or j>=w or V[i][j]or g[i][j]<1:return
  V[i][j]=1;c+=[(i,j)];s.add(g[i][j])
  for a,b in[(0,1),(0,-1),(1,0),(-1,0)]:D(i+a,j+b,c,s)
 for i in range(h):
  for j in range(w):
   if V[i][j]<1 and g[i][j]:c=[];s=set();D(i,j,c,s);C+=[(c,s)]if c else[]
 T=0;S=[]
 for c,s in C:
  if len(s)>1:T=c
  else:S+=[c]
 if not T:return g
 m=min(x[0]for x in T);n=min(x[1]for x in T);P={(i-m,j-n):g[i][j]for i,j in T}
 R=[[0]*w for _ in range(h)]
 for c in S:
  a=min(x[0]for x in c);b=min(x[1]for x in c)
  for(d,e),v in P.items():
   if 0<=a+d<h and 0<=b+e<w:R[a+d][b+e]=v
 return R
