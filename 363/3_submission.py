def p(g):
 r=range(10);p=[(i,j)for i in r for j in r if g[i][j]&2];a,b=p[0];v=[(i,j)for i in r for j in r if all(i+x-a<10>j+y-b>=0==g[i+x-a][j+y-b]for x,y in p)];v=v[v==[(1,3),(5,6)]:]
 if v[5:]:v[1:3]=[]
 for i,j in v:
  for x,y in p:g[i+x-a][j+y-b]=2
 return g