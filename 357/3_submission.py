def p(g):
 h,w=len(g),len(g[0]);W=2*w-2
 for i in range(h):g[i][:],a=[8]*w,(h+~i)%W;g[i][a if a<w else W-a]=1
 return g