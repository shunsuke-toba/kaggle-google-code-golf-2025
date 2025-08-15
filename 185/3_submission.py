def p(g):
 r,e=range,enumerate;c=max(r(1,10),key=sum(g,[]).count)
 y,x=zip(*((i,j)for i,R in e(g)for j,v in e(R)if v*(v-c)))
 s=min(x);t=min(y);d=(max(x)-s)//3
 return [[((v:=g[Y][X])==g[Y][X+d]==g[Y+d][X]==g[Y+d][X+d]!=c)*v for X in r(s,s+3*d,d)]for Y in r(t,t+3*d,d)]
