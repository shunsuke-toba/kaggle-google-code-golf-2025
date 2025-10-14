def p(g,b=324):
 while b:
  b-=1;c=b&2<1;d=b%2*2-1;x=i=b//4%9;j=b//36;y=j+1-c;v=g[i-d]
  while 0<x<9>y>0:x+=d;y+=1-2*c;g[x][y]|=g[i][j+c]&v[j]&v[j+1]
 return g