def p(g):
 w=len(g[0]);h=len(g);t=[]
 def f(r,c):
  if h>r>-1<c<w>g[r][c]==0:g[r][c]=-len(t);t[-1]+=1;f(r+1,c);f(r-1,c);f(r,c+1);f(r,c-1)
 for c in range(w):
  for r in range(h):
   g[r][c]or(t:=t+[0],f(r,c))
 return[[2*(c>1)or t[~c]//max(t)+min(t)//t[~c]*8for c in r]for r in g]
