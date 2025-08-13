def p(g):
 N,M,R=20,0,(0,0,0,0)
 for b in range(N*N):
  r,c=b//N,b%N
  for x in range(r,N):
   for y in range(c,N):
    V,K=0,0
    for i in range(r,x+1):
     for j in range(c,y+1):
      if g[i][j]==0:K=1
      else:V+=1+99*(g[i][j]-1)
     if K:break
    if V>M:M,R=V,(r,c,x,y)
 r,c,x,y=R
 return[[g[i][j]for j in range(c,y+1)]for i in range(r,x+1)]