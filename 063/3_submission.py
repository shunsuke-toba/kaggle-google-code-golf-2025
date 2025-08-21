p=lambda g:[[[x,3][0<i<len(g)-1>j>0and(all(t[j]%3<1for t in g[1:-1])or all(y%3<1for y in r[1:-1]))]for j,x in enumerate(r)]for i,r in enumerate(g)]
