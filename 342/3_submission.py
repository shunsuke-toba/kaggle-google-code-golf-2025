def p(g):
 r,c=divmod(sum(g,[]).index(8),10);a=[-8]*4
 for q in range(100):y,x=q//10,q%10;v=g[y][x];a[(y>r)*2+(x>c)]+=v;g[y][x]=0
 g[r][c],g[r][c+1],g[r+1][c],g[r+1][c+1]=a;return g