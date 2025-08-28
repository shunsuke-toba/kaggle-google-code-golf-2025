def p(g):
 *c,=zip(*g);i=g[4].index(0);n=1
 while c[n:i]!=c[:i-n]:n+=1
 return*zip(*(c[:n]*15)[:15]),