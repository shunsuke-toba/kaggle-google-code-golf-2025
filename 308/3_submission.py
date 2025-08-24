def p(g,E=enumerate):
 b=max(f:=sum(g,[]),key=f.count);s=[0]*20;p=[];m=0
 for i,x in E(g):
  for j,v in E(x):
   if v-b:s[v]+=i;s[~v]+=j;p+=(i,j,v),
 for k,(i,j,v) in E(p):
  i-=s[v]>>2;j-=s[~v]>>2;p[k]=i,j,v;m=max(m,i,-i,j,-j)
 k=2*m+1;o=[[b]*k for _ in[0]*k]
 for i,j,v in p:o[m+i][m+j]=v
 return o
