def p(g):
 R,C=len(g),len(g[0])
 s=[0]*10
 for x in range(10):
  s[x]=[[0]*(C+1)for _ in range(R+1)]
  for r in range(R):
   for c in range(C):s[x][r+1][c+1]=s[x][r][c+1]+s[x][r+1][c]-s[x][r][c]+(g[r][c]==x)
 def q(x,t,l,b,r):return s[x][b+1][r+1]-s[x][t][r+1]-s[x][b+1][l]+s[x][t][l]
 B,M=None,0
 for t in range(R):
  for l in range(C):
   for b in range(t,R):
    for r in range(l,C):
     d={x:q(x,t,l,b,r)for x in range(10)}
     d={x:v for x,v in d.items()if v>0}
     if len(d)>=3:break
     if len(d)==2:
      k=list(d.keys())
      if d[k[0]]<d[k[1]]:k[0],k[1]=k[1],k[0]
      if d[k[0]]<M:continue
      M,B=d[k[0]],(t,l,b,r,k[0],k[1])
 t,l,b,r,j,n=B
 p=[]
 for i in range(t,b+1):
  for u in range(l,r+1):
   if g[i][u]==n:p.append((i-t,u-l))
 w,h=b-t+1,r-l+1
 nr=set(o[0]for o in p)
 nc=set(o[1]for o in p)
 z=[]
 for i in range(w):
  z.append([n if i in nr or u in nc else j for u in range(h)])
 return z