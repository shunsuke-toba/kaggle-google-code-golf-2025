def p(g,f=0):return g[0][f]-g[0][-~f]and[r[::f+2][::-1]for r in g[::f+2]]or p(g,-~f)
