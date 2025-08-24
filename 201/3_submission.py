def p(g):
 h=sum(g,[]);J=S=w=13;(a,b),*_,(c,d)=[divmod(i,w)for i,v in enumerate(h)if v==4]
 for i,v in enumerate(h):
  if v*(v-4)and min((r:=i//w)-a,c-r,(k:=i%w)-b,d-k)<0:
   if r<S:S=r
   if k<J:J=k;t=v==g[a+1][d]
 o=[r[b:d+1]for r in g[a:c+1]]
 for i in range(~a+c):o[i+1][1:-1]=g[S+i][J:J+~b+d][::1-2*t]
 return o