def p(g):
 s={(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v};t=[];d=1,0,-1,0,1
 while s:
  q=[s.pop()];L=[];C=set();a=b=99
  while q:
   i,j=q.pop();L+=[(i,j)];C|={g[i][j]};a=min(a,i);b=min(b,j)
   for k in range(4):
    u=i+d[k];v=j+d[k+1]
    if(u,v)in s:s.remove((u,v));q+=[(u,v)]
  if len(C)>1:P=L;A,B=a,b
  else:t+=[(a,b)]
 O=[]
 for i,j in P:O+=((i-A,j-B,g[i][j]),);g[i][j]=0
 for a,b in t:
  for x,y,v in O:g[a+x][b+y]=v
 return g
