p=lambda g,f=1:g[0][f]==g[0][0]and p(g,f+1)or[r[::~f]for r in g[::f+1]]
