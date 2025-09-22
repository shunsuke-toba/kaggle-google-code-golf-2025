def p(g):
 a=enumerate;R=[(i,j)for i,r in a(g)for j,v in a(r)if(v>2==(c:=i,d:=j))|v%3];a,b=map(max,*R)
 for i,j in R:g[i][j]-=2;g[i+c+~a][j+d+~b]+=2
 return g