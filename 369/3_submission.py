def p(g,n=99):
 def f(r,c):
  if r<10>c>=g[r][c]<1:q[r,c]=g[r][c]=4;f(r-1,c);f(r,c-1);f(r,c+1)
 q={};f(n//10,n%10)
 for r,c in q:g[r][c]-=len(q)
 if n:p(g,n-1);return g