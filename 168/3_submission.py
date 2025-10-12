def p(g,b=324):
 while b:
  b-=1;a=b&1;c=b&2>0;i=b//4%9;j=b//36;x,y=i+a,j+c;v=g[i+1-a]
  while 0<x<9>y>0:x+=2*a-1;y+=2*c-1;g[x][y]|=g[i+a][j+1-c]&v[j]&v[j+1]
 return g