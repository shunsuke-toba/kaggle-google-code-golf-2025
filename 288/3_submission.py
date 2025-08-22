def p(g):
 c=len(g)//2;b=g[-1];s=c-(b[c-1]==b[c]==b[c+1])
 for i in range(s):r=g[i-s-2];r[i]=r[~i]=b[c]
 return g
