def p(g,i=9):
 for r in g:w=len(r)-1;r[i%w^-(i//w&1)]=1;i-=1
 return g