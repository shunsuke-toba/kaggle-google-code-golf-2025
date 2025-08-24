def p(g):
 r=g[0][1]<1;o=[[0]*9for _ in g*3];p=(g[1][0]<1)*5^r*4;q=p^4
 for i in 0,1,2,3:o[r+i][p:p+4]=o[r+4+i][q:q+4]=[3]*4
 return o
