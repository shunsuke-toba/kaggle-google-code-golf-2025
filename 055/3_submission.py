def p(g,k=0):
 for r in g:l=k*3;k+=r[0]>7;r[:]=[(x or 0x10364020>>l*4&15,l:=l+(x>7))[0]for x in r]
 return g