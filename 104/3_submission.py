def p(g):
 r=not any(g[0]);c=not any(r[0]for r in g);d=r==c;o=[[0]*9 for _ in g*3];p=c+4*(d^1);q=c+4*d
 for i in range(4):o[r+i][p:p+4]=o[r+4+i][q:q+4]=[3]*4
 return o
