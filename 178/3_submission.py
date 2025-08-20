def p(g):
 r=[]
 for a in g:r+=[a[:1]]*(r[-1:]!=[a[:1]])
 if r[1:]:return r
 r=[]
 for a in g[0]:r+=[a]*(r[-1:]!=[a])
 return[r]
