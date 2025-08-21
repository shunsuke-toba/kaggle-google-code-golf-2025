p=lambda g:(r:=g[0],([r,[*map(max,r[1:]+[0],[0]+r[:-1])]]*len(g))[:len(g)])[1]
