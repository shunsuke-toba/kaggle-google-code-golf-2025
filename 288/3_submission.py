def p(g):
 t=s=g[-2].count(0)//2
 while s:s-=1;r=g[s-t-2];r[s]=r[~s]=g[-1][t]
 return g