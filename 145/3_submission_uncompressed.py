def p(g):
 t=[]
 def f(r,c):
  if len(g)>r>~0<c<len(g[0])>g[r][c]==0:g[r][c]=~len(t);t[-1]+=1;f(r+1,c);f(r-1,c);f(r,c+1);f(r,c-1)
 for c in range(len(g[0])):
  for r in range(len(g)):
   if len(g)>r>~0<c<len(g[0])>g[r][c]==0:t+=0,;f(r,c)
 for c in range(len(g[0])):
  for r in range(len(g)):
   if len(g)>r>~0<c<len(g[0])>g[r][c]<1:g[r][c]=(t[-g[r][c]-2]==max(t))+((t[-g[r][c]-2]==min(t))<<3)
 return g