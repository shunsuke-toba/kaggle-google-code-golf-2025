def p(g):
 for i in range(96):*g,=zip(*[[(c>0)*(u|c|l|(u>0<l)*(4**(i%4+1)))for u,c,l in zip(a,b,[0,*b])]for a,b in zip([[0]*30]+g,g)][::-1])
 return[[[0,0,0,1,6,2][bin(c).count('1')]if c else 0for c in r]for r in g]