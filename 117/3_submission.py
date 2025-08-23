def p(g):
 w=len(g[0]);f=sum(g,[])
 n=len(f)
 for k in range(w+1,n-w-1):
  if (v:=f[k]) and f.count(v)<6 and v==f[k-w-1]==f[k-w+1]==f[k+w-1]==f[k+w+1]:a,b=divmod(k,w)
 for k,v in enumerate(f):
  if v:r,c=divmod(k,w);g[r][2*b-c]=g[2*a-r][c]=g[2*a-r][2*b-c]=v
 return g
