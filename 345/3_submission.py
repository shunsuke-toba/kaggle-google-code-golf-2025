def p(g,x=0,y=9):
 while y*g[y][x]:a=g[y-1][x]>4;x+=a;y-=1-a;g[y][x]=2
 x<8and p(g,x+1);return g