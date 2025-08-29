def p(j):
 for x in range(64):a=x//8;b=x%8;j[a+1][b+1]>>=j[a][b]*j[a+2][b+2]>0
 return j