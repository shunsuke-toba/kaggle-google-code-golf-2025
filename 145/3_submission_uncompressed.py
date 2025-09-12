def p(g):
 h=len(g);w=len(g[0]);t=[];i=h*w
 def f(y,x):
  if h>y>-1<x<w>g[y][x]==0:g[y][x]=-len(t);t[-1]+=1;f(y+1,x);f(y-1,x);f(y,x+1);f(y,x-1)
 while i:i-=1;g[i//w][i%w]or(t:=t+[0],f(i//w,i%w))
 return[[2*(c>1)or t[~c]//max(t)+min(t)//t[~c]*8for c in r]for r in g]