p=lambda g,f=0:g[0][f]^g[0][f+1]and[r[::-f-2]for r in g[::f+2]]or p(g,f+1)
