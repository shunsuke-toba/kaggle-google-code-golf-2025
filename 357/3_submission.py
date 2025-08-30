def p(g,i=9):
 w=len(g[0])-1
 while~i:r=g[~i]=[8]*-~w;r[~abs(i%(w+w)-w)]=1;i-=1
 return g