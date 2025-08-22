def p(g):
 w=len(g[0]);f=sum(g,[])
 a,b=next((i,j)for i in range(1,len(g)-1)for j in range(1,w-1)if(v:=g[i][j])and f.count(v)<6 and v==g[i-1][j-1]==g[i-1][j+1]==g[i+1][j-1]==g[i+1][j+1])
 for k,v in enumerate(f):
  if v:r,c=divmod(k,w);g[r][2*b-c]=g[2*a-r][c]=g[2*a-r][2*b-c]=v
 return g
