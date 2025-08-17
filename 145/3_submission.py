def p(g):
 h=len(g);w=len(g[0]);r=range;s=[]
 def f(y,x):
  if h>y>=0<=x<w and g[y][x]<1:
   g[y][x]=v;s[-1]+=1;f(y+1,x);f(y-1,x);f(y,x+1);f(y,x-1)
 for y in r(h):
  for x in r(w):
   if g[y][x]<1:s+=0,;v=len(s)+2;f(y,x)
 m=max(s);n=min(s)
 for R in g:
  for x in r(w):
   if (v:=R[x])>2:a=s[v-3];R[x]=a==m or 8*(a==n)
 return g
