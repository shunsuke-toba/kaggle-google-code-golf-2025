def p(g,b=1280):
 while b:b-=1;i=b%8;j=b//8%8;a=b>>6&2;c=b>>7&2;v=g[i+a];g[i+2-a][j+2-c]|=~v[j+1]&v[j+c]&g[i+1][j+1]
 return g