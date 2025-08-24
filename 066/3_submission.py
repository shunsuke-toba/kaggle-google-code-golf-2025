def p(g):
 (a,b),(c,d)=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v==3];f=lambda y,x,a,b,t=2:0<=(y:=y+a)<len(g)and 0<=(x:=x+b)<len(g[a])and((v:=g[y][x])==2 or v==8 and t and(f(y-a,x-b,b,-a,t-1)or f(y-a,x-b,-b,a,t-1)) or v-8 and f(y,x,a,b,t)and(g[y].__setitem__(x,3)or 1));g[a+a-c][b+b-d]-8 and f(a,b,a-c,b-d) or f(c,d,c-a,d-b);return g
