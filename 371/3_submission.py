def p(g):
 a,w=bytes(sum(g,[])),len(g[0]);a=a.find(1)+a.rfind(1)>>1
 for i in-w,-1,0,1,w:b=a+i;g[b//w][b%w]=3
 return g