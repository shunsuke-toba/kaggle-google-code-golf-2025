def p(g):
 n=len(g);r=range(n);c=[g[i][i]for i in r[:n//2]];return[[c[~min(i,j,n+~i,n+~j)]for j in r]for i in r]
