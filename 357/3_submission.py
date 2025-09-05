def p(g,i=9):
 for r in g:w=len(r)-1;r[:]=[8]*-~w;r[~abs(i%(w+w)-w)]=1;i-=1
 return g