def p(g):
 w=len(g[0]);h=len(g);t=[]
 def f(y,x):
  if h>y>-1<x<w>g[y][x]==0:g[y][x]=-len(t);t[-1]+=1;f(y+1,x);f(y-1,x);f(y,x+1);f(y,x-1)
 for y in range(h):
  for x in range(w):
   g[y][x]or(t:=t+[0],f(y,x))
 return[[2*(c>1)or t[~c]//max(t)+min(t)//t[~c]*8for c in r]for r in g]