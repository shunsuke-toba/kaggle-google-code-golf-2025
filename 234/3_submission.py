def p(g):
 for _ in[0]*16:s={0};[len(s:=s|{*r})==3*sum(map(bool,r))and(g.append([0]*len(r)),g.remove(r))for r in g];g=[*zip(*g[::-1])]
 return g
