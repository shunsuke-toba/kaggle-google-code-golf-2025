def p(g):
 n=len(g);h=n//2;R=[g[i][i]for i in range(h)]
 return[[R[h-1-min(r,c,n-1-r,n-1-c)]for c in range(n)]for r in range(n)]

