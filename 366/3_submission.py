def p(g,E=enumerate,R=range,L=len,F=filter):
 s=sum(g,[]);z,y,X=sorted({*s},key=s.count)[-3:];t=lambda q:[*map(list,zip(*F(q,zip(*F(q,g)))))]
 a,b=[t(lambda r:c in r)for c in(y,X)];n,m,p=L(a)-1,L(a[0])-1,[]
 for i in R(n):
  for j in R(m):
   if y not in(a[i][j],a[i+1][j],a[i][j+1]):
    k,l=i,j
    while k<n and a[k+1][l]-y:k+=1
    while l<m and a[k][l+1]-y:l+=1
    q=a[i:k+1];p+=[r[j:l+1]for r in q],
    for r in q:r[j:l+1]=[y]*(l-j+1)
 for r in sorted(p,key=lambda r:-sum(c!=z for c in sum(r,[]))):
  n,m=L(r),L(r[0])
  for i in R(L(b)-n+1):
   for j in R(L(b[0])-m+1):
    if all(b[i+u][j+v]==(X,c)[c!=z]for u,s in E(r)for v,c in E(s)):
     for k,s in E(r):b[i+k][j:j+m]=s
 return b