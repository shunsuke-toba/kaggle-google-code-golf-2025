p=lambda g:(r:=g[0],s:=list(map(max,r[1:]+[0],[0]+r[:-1])),([r,s]*len(g))[:len(g)])[2]
