def p(g):
 r=range;n=len(g)
 return[[[g[i][j],3][0<i<n-1and 0<j<n-1and(all(g[y][j]%3<1for y in r(1,n-1))or all(x%3<1for x in g[i][1:-1]))]for j in r(n)]for i in r(n)]
