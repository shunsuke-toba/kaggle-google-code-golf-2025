def p(g):
 a=[i for i,c in enumerate(zip(*g))if max(map(c.count,R:=range(1,10)))>len(g)-3];b=[i for i,r in enumerate(g)if max(map(r.count,R))>len(g[0])-3];g=[r[a[0]:a[1]+1]for r in g[b[0]:b[1]+1]];h=len(g);w=len(g[0]);W=w-2;D={g[0][1]:(-1,0),g[-1][1]:(1,0),g[1][0]:(0,-1),g[1][-1]:(0,1)}
 for k in range((h-2)*W):
  i,j=k//W+1,k%W+1
  while(d:=D.get(c:=g[i][j]))and h>(i:=i+d[0])>=0<=(j:=j+d[1])<w:g[i][j]=c
 return g
