def p(g):
 r,c=divmod(sum(g,[]).index(8),10);q=100
 while q:
  q-=1;y,x=q//10,q%10;v=g[y][x];g[y][x]=0
  if v&7:g[r+(y>r)][c+(x>c)]=v
 return g
