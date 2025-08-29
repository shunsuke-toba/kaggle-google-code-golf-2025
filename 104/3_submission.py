def p(g):
 r=g[0][1]<1;o=[[0]*9for _ in g*3];i=8
 while i:i-=1;s=4*r^-g[1][2]&5^i&4;o[r+i][s:s+4]=[3]*4
 return o