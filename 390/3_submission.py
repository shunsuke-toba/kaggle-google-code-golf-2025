def p(g,e=enumerate):
 for y,x in[(i,j)for i,r in e(g)for j,v in e(r)if v&4]:_,i,j=min((abs(x-j+y-i),i,j)for i,r in e(g)for j,v in e(r)if(i==y or j==x)*v&2);g[2*i-y][2*j-x],g[y][x]=5,0
 return g