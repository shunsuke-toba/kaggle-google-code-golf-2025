def p(g):
 h=len({*g[0]})>1
 if h:g=[*zip(*g)]
 r=[]
 for a in g:r+=[a[:1]]*(r[-1:]!=[a[:1]])
 return[sum(r,())]if h else r
