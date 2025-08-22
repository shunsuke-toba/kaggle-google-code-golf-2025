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
 for R in g:
  for x in r(w):
   if (v:=R[x])>2:a=s[v-3];R[x]=(a==m)+8*(a==n)
 return g
