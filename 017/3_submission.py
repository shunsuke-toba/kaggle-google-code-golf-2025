def p(g,s=1):
 q=range(len(g));d={};return[[d[i%s,j%s]for j in q]for i in q]if all((v:=g[i][j])<1 or d.setdefault((i%s,j%s),v)==v for j in q for i in q)else p(g,s+1)
