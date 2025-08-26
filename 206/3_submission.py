def p(g):
 a=b=9;e=enumerate;[v-5 and(a:=min(a,i),b:=min(b,j))or(s:=i-1,t:=j-1)for i,r in e(g)for j,v in e(r)if v]
 for k in 0,1,2:g[s+k][t:t+3]=g[a+k][b:b+3]
 return g