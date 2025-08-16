def p(g):
 n=len(g);R=range(n-1);r,c=next((i,j)for i in R for j in R if g[i][j]&g[i][j+1]&g[i+1][j]&g[i+1][j+1]&3);s=lambda i,j,I,J:(n>(i:=i+I)>-1<(j:=j+J)<n)and(g[i][j]or g[i].__setitem__(j,s(i,j,I,J))or g[i][j])
 for _ in 0,1,2,3:a,b=divmod(_,2);s(r+a,c+b,2*a-1,0);s(r+a,c+b,0,2*b-1)
 return g