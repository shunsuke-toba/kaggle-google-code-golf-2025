def p(g,R=range):
 d=1,0,-1,0
 e=1,-1,-1,1
 for b in R(9**5):
  i,j,k=b%9%8+1,b%89%8+1,b%4
  if all(g[i+d[l]][j+d[l-3]]==0 for l in R(4))and g[i+e[k]][j+e[k-3]]>0:g[i-e[k]][j-e[k-3]]=g[i][j]
 return g
