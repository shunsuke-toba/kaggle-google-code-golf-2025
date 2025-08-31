def p(g):
 a,w=bytes(sum(g,[])),len(g[0]);i=a.find(1)+a.rfind(1)>>1
 for a in i-w,i-1,i,i+1,i+w:g[a//w][a%w]=3
 return g