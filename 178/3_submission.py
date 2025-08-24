def p(g):
 h=g[1:]==g[:-1];r=[]
 for a in(g,zip(*g))[h]:r+=[a[0]]*(r[-1:]!=[a[0]])
 return([*zip(r)],[r])[h]
