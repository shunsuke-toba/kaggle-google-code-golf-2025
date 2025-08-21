def p(g):
 s=sum(g,[]);exec("while~-(min({*s}-{0},key=s.count)in g[-1]):g.pop()\ng[:]=[*map(list,zip(*g[::-1]))]\n"*4)
 return g