def p(g):
 r=g[0][1]<1;p=4*r^-g[1][2]&5;o=[[0]*9for _ in g*3]
 for i in range(8):s=p^i&4;o[r+i][s:s+4]=4*[3]
 return o