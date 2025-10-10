def p(g,b=9**4):
 while b:
  b-=1;i,j,a,c=b%9,b//9%9,b>>6&1,b>>7&1;x,y=i+a,j+c
  while 0<x<9>y>0:x+=2*a-1;y+=2*c-1;v=g[i+1-a];g[x][y]|=g[i+a][j+1-c]&v[j+1-c]&v[j+c]
 return g