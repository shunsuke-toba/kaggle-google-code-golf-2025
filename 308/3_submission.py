def p(g,E=enumerate):
 m=~-len(g)//5;k=2*m+1;o=[[b:=max(g[0],key=g[0].count)]*k for _ in[0]*k];s=[0]*20;p=[]
 for i,x in E(g):
  for j,v in E(x):
   if v-b:s[v]+=i;s[~v]+=j;p+=(i,j,v),
 for i,j,v in p:o[m+i-s[v]//4][m+j-s[~v]//4]=v
 return o