def p(g):
 a=enumerate;R=[(i,j)for i,r in a(g)for j,v in a(r)if(v>2<(c:=i-5)+(d:=j-5)<0)+v%3][::-1];a,b=map(min,zip(*R))
 for i,j in R:g[i][j]=0;g[i+c-a][j+d-b]=2
 return g