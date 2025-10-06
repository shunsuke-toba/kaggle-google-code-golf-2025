def p(g,y=64):
 while y:y-=1;b,c,d,*_=g[y>>3:];c[y%8+1]>>=b[y%8]*d[-8|y]>0
 return g