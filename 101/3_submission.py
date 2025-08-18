def p(g,R=range):
 n,m=len(g),len(g[0]);x1,y1,x2,y2=99,99,0,0;d=1,0,-1,0;u=set()
 for b in R(9**5):
  i,j,k=b%97%n,b%89%m,b%4
  def c(x,y): return 0<=x<n and 0<=y<m
  r,q=d[k],d[k-3]
  if g[i][j]==1or(g[i][j]==2and(c(i+r,j+q)and g[i+r][j+q]==1or(i+r,j+q)in u)):
   x1,y1,x2,y2=min(x1,i),min(y1,j),max(x2,i),max(y2,j)
   if g[i][j]==2:u.add((i,j))
 P=[r[y1:y2+1]for r in g[x1:x2+1]];N=len(u)
 for s in[3,2,1]:
  P2=[[P[i//s][j//s]for j in R(len(P[0])*s)]for i in R(len(P)*s)];s1,s2=len(P2),len(P2[0])
  for b in R(n*m*9):
   i,j=b//(3*m)-n,b%(3*m)-m;o=1;c=0
   for z in R(s1*s2):
    x,y=z//s2,z%s2
    if c(i+x,j+y)and(i+x,j+y)not in u:
     if g[i+x][j+y]!=P2[x][y]//2*2:o=0
     elif P2[x][y]==2:c+=1
   if o and c==N*s*s:
    for z in R(s1*s2):
     x,y=z//s2,z%s2
     if c(i+x,j+y):g[i+x][j+y]=P2[x][y];u.add((i+x,j+y))
 return g