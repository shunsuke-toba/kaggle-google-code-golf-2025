def p(g,E=enumerate,M=max):
 f=sum(g,[]);b=M(f,key=f.count);s=[0]*20;p=[]
 for i,x in E(g):
  for j,v in E(x):
   if v-b:s[v]+=i;s[v+10]+=j;p+=(i,j,v),
 m=0
 for k,(i,j,v) in E(p):
  i-=s[v]>>2;j-=s[v+10]>>2;p[k]=i,j,v;m=M(m,i,-i,j,-j)
 k=2*m+1;o=[[b]*k for _ in[0]*k]
 for i,j,v in p:o[m+i][m+j]=v
 return o
