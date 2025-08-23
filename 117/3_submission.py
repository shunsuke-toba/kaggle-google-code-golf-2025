def p(g):
 w=len(g);f=sum(g,[])
 for k in range(w+1,~w+len(f)):
  if (v:=f[k])and v==f[k-w-1]==f[k-w+1]==f[k+w-1]==f[k+w+1]:a=k//w;b=k%w
 for k,v in enumerate(f):
  if v:r=k//w;c=k%w;g[r][2*b-c]=g[2*a-r][c]=g[2*a-r][2*b-c]=v
 return g
