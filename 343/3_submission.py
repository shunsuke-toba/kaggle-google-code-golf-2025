def p(g):
 *g,=filter(sum,zip(*g));n=6+2*(g[6:]!=g[:-6])
 return*zip(*(g[:n]*5)[:15]),