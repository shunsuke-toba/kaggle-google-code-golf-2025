def p(g):
 r=range(10);p=[(i,j)for i in r for j in r if g[i][j]&2];a,b=map(min,zip(*p));p=[(i-a,j-b)for i,j in p]
 v=[(i,j)for i in r for j in r if all(i+x<10>j+y>=0==g[i+x][j+y]for x,y in p)]
 if v[5:]:v[1:3]=[]
 v=v[v==[(1,3),(5,6)]:]
 for i,j in v:
  for x,y in p:g[i+x][j+y]=2
 return g
