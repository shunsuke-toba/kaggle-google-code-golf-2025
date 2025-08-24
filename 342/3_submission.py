def p(g):
 r,c=divmod(sum(g,[]).index(8),10);a=[-8]*4
 for q in range(100):y,x=q//10,q%10;a[(y>r)<<1|(x>c)]+=g[y][x];g[y][x]=0
 g[r][c:c+2]=a[:2];g[r+1][c:c+2]=a[2:];return g
