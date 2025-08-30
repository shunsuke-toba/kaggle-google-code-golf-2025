def p(g,i=9):
 w=len(g[0])-1
 while~i:g[~i][~abs(i%(w+w)-w)]=1;i-=1
 return g