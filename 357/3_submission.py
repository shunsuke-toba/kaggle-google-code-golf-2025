def p(g,L=len):
 h,w=L(g),L(g[0]);W=2*w-2
 r=[[8]*w for _ in g]
 for i in range(h):a=(h+~i)%W;r[i][a if a<w else W-a]=1
 return r