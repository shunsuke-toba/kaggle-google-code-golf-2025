def p(g):
 h=len(g);w=len(g[0])
 G=[(i,j)for i in range(h)for j in range(w)if g[i][j]==3]
 R=[(i,j)for i in range(h)for j in range(w)if g[i][j]==2]
 if not(G and R):return g
 G.sort();R.sort()
 D=[(-1,0),(1,0),(0,-1),(0,1)]if len(G)<2 else[(0,-1),(0,1)]if G[0][0]==G[1][0]and sum(r[1]for r in R)//len(R)<G[0][1]else[(0,1),(0,-1)]if G[0][0]==G[1][0]else[(-1,0),(1,0)]
 for d in D:
  for s in G:
   W=[r[:]for r in g]
   def F(i,j,u,v,A,t):
    o=0
    while 1:
     x,y=i+u,j+v
     if x<0 or x>=h or y<0 or y>=w:break
     if A[x][y]==2:return 1
     if A[x][y]==8:o=1;break
     if A[x][y]==3:break
     if A[x][y]<1:A[x][y]=3;i,j=x,y
     else:break
    if o and t:
     L=[]
     for a,b in[(-1,0),(1,0),(0,-1),(0,1)]:
      if(a,b)in[(u,v),(-u,-v)]:continue
      m=min(abs(i+a-r[0])+abs(j+b-r[1])for r in R)
      L+=[(m,a,b)]
     L.sort()
     for _,a,b in L:
      B=[r[:]for r in A]
      if F(i,j,a,b,B,t-1):
       for x in range(h):
        for y in range(w):
         if B[x][y]==3>g[x][y]:A[x][y]=3
       return 1
    return 0
   if F(s[0],s[1],d[0],d[1],W,2):return W
 return g
