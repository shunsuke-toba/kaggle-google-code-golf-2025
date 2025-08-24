def p(g):
 a=enumerate;R=[(i,j)for i,r in a(g)for j,v in a(r)if v%3 or v>2and(c:=i-5,d:=j-5)and 0]
 a,b=map(min,zip(*R))
 for i,j in R[::-1]:g[i][j]=0;g[i+c-a][j+d-b]=2
 return g
