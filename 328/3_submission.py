def p(g,R=range):
 n=len(g);P=[(a,b,g[a][b])for a in(0,n-1)for b in(0,n-1)if g[a][b]];M=[[min(max(abs(i-x),abs(j-y))for x,y,_ in P)for j in R(n)]for i in R(n)]
 def u(i,j):
  if(0<=i<n)&(0<=j<n)and M[i][j]>=r:
   if not(q:=C.get((i,j)))or t<q[0]:C[i,j]=(t,c)
   elif(t==q[0])*(q[1]^c):C[i,j]=(t,0)
 for r in R(0,n,2):
  C={}
  for x,y,c in P:
   for t in R(r+1):u(x+(X:=1-2*(x>0))*r,y+(Y:=1-2*(y>0))*t);u(x+X*t,y+Y*r)
  for (i,j),k in C.items():g[i][j]=k[1]
 return g