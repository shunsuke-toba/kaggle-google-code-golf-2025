def p(g):
 g=sum(g,[])
 z=[i for i in range(89)if g.count(g[i])<2]
 for a,b,o in zip(z,z[::-1],[22,18,-18,-22]):g[a],g[b+o]=0,g[a]
 return list(zip(*[iter(g)]*10))