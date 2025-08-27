def p(g):
 r=[]
 for a,*_ in(g,zip(*g))[h:=g[1:]==g[:-1]]:r+=[a]*(r[-1:]!=[a])
 return h*[r]or[*zip(r)]