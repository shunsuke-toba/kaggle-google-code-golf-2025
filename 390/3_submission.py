def p(g):
 e=enumerate;R=[(i,j)for i,r in e(g)for j,v in e(r)if v==2]
 for y,x in[(i,j)for i,r in e(g)for j,v in e(r)if v>2]:i,j=min((abs(x-j+y-i),i,j)for i,j in R if i==y or j==x)[1:];g[y][x],g[2*i-y][2*j-x]=0,5
 return g
