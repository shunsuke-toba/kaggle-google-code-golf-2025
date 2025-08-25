def p(g):
 a=b=s=t=9;e=enumerate;[5==v and(s:=i-1,t:=j-1)or v and(a:=min(a,i),b:=min(b,j))for i,r in e(g)for j,v in e(r)]
 for k in 0,1,2:g[s+k][t:t+3]=g[a+k][b:b+3]
 return g
