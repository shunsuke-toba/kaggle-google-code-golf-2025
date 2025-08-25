def p(g):
 h=g[1:]==g[:-1];r=[]
 for a,*_ in(g,zip(*g))[h]:r+=[a]*(r[-1:]!=[a])
 return([*zip(r)],[r])[h]