def p(g):
 n=len(g);r,c=divmod(sum(g,[]).index(3),n);s=lambda i,j,I,J:n>(i:=i+I)>-1<(j:=j+J)<n and(g[i][j]or g[i].__setitem__(j,s(i,j,I,J))or g[i][j])
 for _ in 0,1,2,3:a=_>1;b=_&1;s(r+a,c+b,2*a-1,0);s(r+a,c+b,0,2*b-1)
 return g
