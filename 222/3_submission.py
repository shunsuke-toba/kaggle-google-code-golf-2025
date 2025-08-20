def p(g):
 w=len(g[0])-1;d=[0]*10
 for a,b in zip(g,g[1:]):
  for x in range(w):
   if(v:=a[x])==a[x+1]==b[x]==b[x+1]:d[v]+=1
 o=[[0]*-~w for _ in g]
 for a,b,c,e in zip(g,g[1:],o,o[1:]):
  for x in range(w):
   if(v:=a[x])==a[x+1]==b[x]==b[x+1]and d[v]>1:c[x]=c[x+1]=e[x]=e[x+1]=v
 return o
