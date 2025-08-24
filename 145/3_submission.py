def p(g):
 h=len(g);w=len(g[0]);t=[]
 def f(y,x):
  if h>y>-1<x<w>g[y][x]==0:
   g[y][x]=v;t[-1]+=1
   for d in 1,-1:f(y+d,x);f(y,x+d)
 for i in range(h*w):
  if g[i//w][i%w]==0:v=~len(t);t+=0,;f(i//w,i%w)
 return[[2*(c>1)or t[~c]//max(t)+min(t)//t[~c]*8 for c in r]for r in g]
