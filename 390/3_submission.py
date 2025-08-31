def p(g,e=range(15)):
 for y,x,v in(a:=[(i,j,g[i][j])for i in e for j in e]):
  if v&4:_,i,j=min((abs(x-j+y-i),i,j)for i,j,u in a if(i==y or j==x)*u&2);g[2*i-y][2*j-x],g[y][x]=5,0
 return g