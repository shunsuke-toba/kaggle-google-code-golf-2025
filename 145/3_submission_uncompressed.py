def p(g):
 t=[]
 def f(r,c):
  if len(g)>r>~0<c<len(g[0])>g[r][c]==0:g[r][c]=~len(t);t[-1]+=1;f(r+1,c);f(r-1,c);f(r,c+1);f(r,c-1)
 for c in range(len(g[0])):
  for r in range(len(g)):
   if g[r][c]==0:t+=0,;f(r,c)
 return[[2*(c>1)or (t[-c-2]==max(t))or (t[-c-2]==min(t))*8for c in r]for r in g]