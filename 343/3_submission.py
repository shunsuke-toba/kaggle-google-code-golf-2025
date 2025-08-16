def p(g):
 R=range(len(g[0]));k=max(j for j in R for r in g if r[j])+1;n=1
 while any(r[j]!=r[j%n]for j in R[:k]for r in g):n+=1
 return[[r[j%n]for j in R]for r in g]
