def p(g):
 a=bytes(sum(g,[]));w=len(g[0])
 for i in-w,-1,0,1,w:b=(a.find(1)+a.rfind(1)>>1)+i;g[b//w][b%w]=3
 return g