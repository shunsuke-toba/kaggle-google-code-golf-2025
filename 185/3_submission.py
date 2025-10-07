def p(g):
 for z in[{*g[0]}]*2:g=[c for c in zip(*g)if{*c}-z]
 return[[B[j]*(B[j]==B[j+1]==D[j]==D[j+1]!=max(z))for j in(0,1,2)]for B,D in zip(g,g[1:])]