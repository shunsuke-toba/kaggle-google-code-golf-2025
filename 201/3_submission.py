def p(g):
 W=len(g[0]);f=sum(g,[])
 t=[divmod(i,W)for i,v in enumerate(f)if v==4];(a,b),(c,d)=t[0],t[-1];R=g[a+1][d]
 s=[divmod(i,W)for i,v in enumerate(f)if v and v-4 and not(a<=i//W<=c and b<=i%W<=d)]
 S,J=map(min,zip(*s))
 o=[r[b:d+1]for r in g[a:c+1]]
 f=g[min(i for i,j in s if j==J)][J]==R
 for k in range(c-a-1):r=g[S+k][J:J+d-b-1];o[k+1][1:-1]=r[::-1]if f else r
 return o
