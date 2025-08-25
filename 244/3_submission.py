p=lambda g,f=1:g[0][~-f]^g[0][f]and[r[::~f]for r in g[::f+1]]or p(g,f+1)
