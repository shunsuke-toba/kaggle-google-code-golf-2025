def p(g):
 h=g[9];j=h.index(max(h))
 for r in g:r[j::2]=[h[j]]*(5-j//2);c=j+1;k=0
 while c<10:g[k][c]=5;k=~k;c+=2
 return g
