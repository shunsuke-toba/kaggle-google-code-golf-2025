def p(g):
 c=[0]*10
 for v in sum(g,[]):c[v]+=v>0
 m=max(c)
 return[[*dict.fromkeys(v for v in sum(zip(*g),()) if m==c[v]>0)]]*m
