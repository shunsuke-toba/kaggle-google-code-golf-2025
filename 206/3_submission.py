def p(g):
 e=enumerate;h=[(i,j)for i,r in e(g)for j,v in e(r)if v*(v-5or(s:=i,t:=j)*0)];a,b=map(min,*h)
 for i,j in h:g[i+s+~a][j+t+~b]=g[i][j]
 return g