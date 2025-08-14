def p(g):
 h,w=len(g),len(g[0]);f=sum(g,[]);a,b=next((i,j)for i in range(1,h-1)for j in range(1,w-1)if(v:=g[i][j])and f.count(v)<6 and v==g[i-1][j-1]==g[i-1][j+1]==g[i+1][j-1]==g[i+1][j+1]and g[i-1][j]==g[i+1][j]==g[i][j-1]==g[i][j+1]==0);s=[*map(list,g)]
 for k in range(h*w):
  if v:=s[r:=k//w][c:=k%w]:g[r][2*b-c]=g[2*a-r][c]=g[2*a-r][2*b-c]=v
 return g
