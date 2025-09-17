def p(g):
 g=[*filter(sum,zip(*g))];n=3
 while g[n:]!=g[:-n]:n+=1
 return*zip(*(g[:n]*5)[:15]),