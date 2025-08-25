def p(g):
 j=g[9].index(c:=max(g[9]));k=0
 for r in g:r[j::2]=[c]*(5-j//2)
 while j<9:g[k][j+1]=5;k=~k;j+=2
 return g
