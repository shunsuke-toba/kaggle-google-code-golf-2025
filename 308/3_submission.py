def p(g,R=range,E=enumerate,M=max):
 t=sum(g,[]);d=M(R(10),key=t.count);a=[99]*10;b=[99]*10;A=[-99]*10;B=[-99]*10;P=[]
 for i,r in E(g):
  for j,v in E(r):
   if v!=d:P+=[(i,j,v)];a[v]=min(a[v],i);A[v]=M(A[v],i);b[v]=min(b[v],j);B[v]=M(B[v],j)
 s=M(M(A[c]-a[c],B[c]-b[c])for c in R(10)if A[c]>-99)+1;k=(s-1)//2;o=[[d]*s for _ in R(s)]
 for i,j,v in P:o[i-((a[v]+A[v])//2)+k][j-((b[v]+B[v])//2)+k]=v
 return o