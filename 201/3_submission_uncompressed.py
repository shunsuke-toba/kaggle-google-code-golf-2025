def p(g):
 s=j=13
 t=1
 for y,row in enumerate(g):
  for x,v in enumerate(row):
   if v==4:
    if t:a,b=y,x;t=0
    c,d=y,x
 o=[r[b:d+1]for r in g[a:c+1]]
 for y,row in enumerate(g):
  for x,v in enumerate(row):
   if y-a|c-y|x-b|d-x<0<v:
    if y<s:s=y
    if x<j:j=x;f=v!=o[1][0]
 for r in o[1:-1]:
  s+=1;r[1:-1]=g[s-1][j:j+d-b-1][::1-2*f]
 return o