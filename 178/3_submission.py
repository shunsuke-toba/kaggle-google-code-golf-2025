def p(g):
 h=len({*g[0]})>1;r=[]
 for a in(g,g:=zip(*g))[h]:r+=[a[:1]]*(r[-1:]!=[a[:1]])
 return (r,[*zip(*r)])[h]
