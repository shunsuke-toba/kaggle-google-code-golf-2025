def p(g,E=enumerate):
 b=max(f:=sum(g,[]),key=f.count);s=[0]*20;p=[]
 for i,x in E(g):
  for j,v in E(x):
   if v-b:s[v]+=i;s[~v]+=j;p+=(i,j,v),
 m=max(p:=[(i-s[v]//4,j-s[~v]//4,v)for i,j,v in p])[0]
 k=2*m+1;o=[[b]*k for _ in[0]*k]
 for i,j,v in p:o[m+i][m+j]=v
 return o