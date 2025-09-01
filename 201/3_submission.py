def p(g):
 j=s=w=13;h=bytes(sum(g,[]));a=h.find(4);b=a%w;a//=w;c=h.rfind(4);d=c%w;c//=w;o=[r[b:-~d]for r in g[a:-~c]]
 for i,v in enumerate(h):r=i//w;k=i%w;v&-5 and r-a|c-r|k-b|d-k<0 and(s:=min(s,r),k<j and(j:=k,f:=v!=o[1][0]))
 for r in o[1:-1]:r[1:-1]=g.pop(s)[j:j+~b+d][::1-2*f]
 return o