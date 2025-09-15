def p(g):
 *_,b=g;t=s=b.count(b[0])//2
 while s:s-=1;r=g[s-t-2];r[s]=r[~s]=b[t]
 return g