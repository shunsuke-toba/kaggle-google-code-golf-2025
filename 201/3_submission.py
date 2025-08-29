def p(g):
 J=S=w=13;h=sum(g,[]);(a,b),*_,(c,d)=[divmod(i,w)for i in range(169)if h[i]==4];o=[r[b:d+1]for r in g[a:c+1]]
 for i,v in enumerate(h):
  r=i//w;k=i%w
  if v&-5 and(r-a|c-r|k-b|d-k)<0:S=min(S,r);k<J and(J:=k,t:=v==o[1][-1])
 for r,y in zip(o[1:-1],g[S:]):r[1:-1]=y[J:J+~b+d][::1-2*t]
 return o