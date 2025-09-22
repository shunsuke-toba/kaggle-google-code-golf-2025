def p(g):
 e=enumerate;a,b=map(min,*[(i,j)for i,r in e(g)for j,v in e(r)if v*(v-5or(s:=i,t:=j)*0)])
 for k in-1,0,1:g[s+k][t-1:t+2]=g[a-~k][b:b+3]
 return g