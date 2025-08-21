def p(g):
 f=lambda x,R=range(1,10):[i for i,s in enumerate(x)if max(map(s.count,R))>len(s)-3];x,y=f(zip(*g));u,v=f(g);g=[r[x:y+1]for r in g[u:v+1]];h=len(g);W=len(g[0])-2;D={g[0][1]:(-1,0),g[-1][1]:(1,0),g[1][0]:(0,-1),g[1][-1]:(0,1)}
 for k in range((h-2)*W):
  i,j=k//W+1,k%W+1
  while(d:=D.get(c:=g[i][j]))and h>(i:=i+d[0])>=0<=(j:=j+d[1])<W+2:g[i][j]=c
 return g
