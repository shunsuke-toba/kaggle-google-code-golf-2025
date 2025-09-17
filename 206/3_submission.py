def p(g):
 e=enumerate;a,b=map(min,zip(*((i,j)for i,r in e(g)for j,v in e(r)if v*(v-5or((s:=i-1)-(t:=j-1))*0))))
 for k in 0,1,2:g[s+k][t:t+3]=g[a+k][b:b+3]
 return g