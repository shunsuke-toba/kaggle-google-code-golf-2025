def p(g):
 h=len(g);w=len(g[0]);r=range;s=[]
 def F(y,x):
  if h>y>=0<=x<w and g[y][x]<1:
   g[y][x]=v;s[-1]+=1
   for d in 1,-1:F(y+d,x);F(y,x+d)
 for y in r(h):
  for x in r(w):
   if g[y][x]<1:s+=0,;v=len(s)+2;F(y,x)
 m=max(s);n=min(s)
 return [[2if v==2else (a:=s[v-3])==m or a==n and 8 for v in R]for R in g]
