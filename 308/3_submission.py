def p(g,R=range,E=enumerate,A=abs,M=max):
 f=sum(g,[]);b=M(R(10),key=f.count);r=[0]*10;c=[0]*10;p=[]
 for i,x in E(g):
  for j,v in E(x):
   if v-b:r[v]+=i;c[v]+=j;p+=[(i,j,v)]
 m=0
 for k,(i,j,v) in E(p):
  i-=r[v]>>2;j-=c[v]>>2;p[k]=i,j,v;m=M(m,A(i),A(j))
 k=2*m+1;o=[[b]*k for _ in R(k)]
 for i,j,v in p:o[m+i][m+j]=v
 return o
