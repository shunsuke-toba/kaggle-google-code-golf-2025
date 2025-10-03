def p(g):
 for z in({*g[0]},)*2:g=[c for c in zip(*g)if{*c}-z]
 return[[a*(a==b==c==d!=max(z))for a,b,c,d in zip(B,B[1:],D,D[1:])]for B,D in zip(g,g[1:])]