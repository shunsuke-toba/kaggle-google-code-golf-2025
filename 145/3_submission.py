def p(g):
 h=len(g);w=len(g[0]);r=range;t=[]
 def f(y,x):
  if h>y>=0<=x<w>g[y][x]<1:
   g[y][x]=v;t[-1]+=1
   for d in 1,-1:f(y+d,x);f(y,x+d)
 for y in r(h):
  for x in r(w):
   if g[y][x]<1:t+=0,;v=len(t)+2;f(y,x)
 M=max(t);m=min(t)
 return [[2*(c==2)or((a:=t[c-3])==M or(a==m)*8)for c in R]for R in g]
