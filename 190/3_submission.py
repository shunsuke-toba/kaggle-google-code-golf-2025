def p(g,b=1280):
 while b:b-=1;i=b%8+1;j=b//8%8+1;a=b>>6&1or-1;c=b>>7&1or-1;v=g[i+a];g[i-a][j-c]|=(v[j+c]>v[j])*g[i][j]
 return g