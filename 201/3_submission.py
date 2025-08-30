def p(g):
 j=s=w=13;h=sum(g,[]);(a,b),*_,(c,d)=[(i//w,i%w)for i in range(169)if h[i]==4];o=[r[b:d+1]for r in g[a:c+1]]
 for i,v in enumerate(h):r=i//w;k=i%w;v&-5 and(r-a|c-r|k-b|d-k)<0 and(s:=min(s,r),k<j and(j:=k,f:=v!=o[1][0]))
 for r,y in zip(o[1:-1],g[s:]):r[1:-1]=y[j:j+~b+d][::1-2*f]
 return o