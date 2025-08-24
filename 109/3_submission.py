def p(g):
 n=len(g)//2;return[[g[0][n]*(e>0)for e in r[:n]+r[n-1::-1]]for r in g[:n]+g[:n][::-1]]
