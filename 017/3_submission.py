def p(g,s=1):r=range(21);d={};return all((v:=g[i][j])<1 or d.setdefault((i%s,j%s),v)==v for j in r for i in r)and[[d[i%s,j%s]for j in r]for i in r]or p(g,s+1)
