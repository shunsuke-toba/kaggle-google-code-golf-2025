def p(g):
 r=g[0][1]<1;p=(g[1][0]<1)*5^r*4;o=[[0]*9for _ in g*3]
 for i in range(8):s=p^i&4;o[r+i][s:s+4]=4*[3]
 return o
