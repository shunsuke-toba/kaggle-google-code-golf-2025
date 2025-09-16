def p(g):
 c=[*zip(*g)][:g[4].index(0)];n=3
 while c[n:]!=c[:-n]:n+=1
 return*zip(*(c[:n]*5)[:15]),