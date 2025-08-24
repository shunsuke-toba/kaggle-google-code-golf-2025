def p(g):
 o=[[0]*9for _ in g*3];p=(g[1][0]<1)*5^(r:=g[0][1]<1)*4
 for i in range(8):o[r+i][p^i//4*4:(p^i//4*4)+4]=[3]*4
 return o
