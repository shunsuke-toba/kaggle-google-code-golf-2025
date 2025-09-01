def p(g,E=enumerate):
 m=(len(g[0])+4)//5-1;b=max(g[0],key=g[0].count);s=[0]*20;p=[];k=2*m+1;o=[[b]*k for _ in[0]*k]
 for i,x in E(g):
  for j,v in E(x):
   if v-b:s[v]+=i;s[~v]+=j;p+=(i,j,v),
 for i,j,v in p:o[m+i-s[v]//4][m+j-s[~v]//4]=v
 return o