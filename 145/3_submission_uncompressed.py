def p(g):
 h=len(g);w=len(g[0]);t=[]
 def f(r,c):
  if h>r>-1<c<w>g[r][c]==0:g[r][c]=-len(t);t[-1]+=1;f(r+1,c);f(r-1,c);f(r,c+1);f(r,c-1)
 for r in range(h):
  for c in range(w):
   g[r][c]or(t:=t+[0],f(r,c))
 return[[2*(c>1)or t[~c]//max(t)+min(t)//t[~c]*8for c in r]for r in g]
