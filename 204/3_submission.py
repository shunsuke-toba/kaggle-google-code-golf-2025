def p(g):
 n=len(g);f=range;R=f(n)
 for r in R:
  for c in R:
   for s in f(3,n):
    if r+s<=n>=c+s and all({g[r][c+i],g[r+s-1][c+i],g[r+i][c],g[r+i][c+s-1]}=={1}for i in f(s)):
     for i in f(r+1,r+s-1):g[i][c+1:c+s-1]=[2|s%2*5]*(s-2)
 return g