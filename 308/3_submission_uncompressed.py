#0
def p(g,E=enumerate):
 m=~-len(g)//5;k=2*m+1;o=[[b:=max(g[0],key=g[0].count)]*k for _ in[0]*k];s=[0]*20
 for i,r in E(g):
  for j,v in E(r):
   if v-b:s[v]+=i;s[~v]+=j
 for i,r in E(g):
  for j,v in E(r):
   if v-b:o[m+i-s[v]//4][m+j-s[~v]//4]=v
 return o
