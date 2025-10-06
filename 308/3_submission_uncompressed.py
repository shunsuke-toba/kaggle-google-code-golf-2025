def p(g):
 m=~-len(g)//5;k=m+-~m;o=[[b:=max(g[0],key=g[0].count)]*k for _ in[0]*k];s=[0]*20
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v^b:s[v]+=i;s[~v]+=j
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v^b:o[m+i-s[v]//4][m+j-s[~v]//4]=v
 return o