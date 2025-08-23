def p(g,E=enumerate,R=range,L=len,F=filter):
 s=sum(g,[]);z,y,X=sorted({*s},key=s.count)[-3:];t=lambda q:[*map(list,zip(*F(q,zip(*F(q,g)))))]
 a=t(lambda r:y in r);b=t(lambda r:X in r);n,m,p=L(a),L(a[0]),[]
 for i in R(n-1):
  for j in R(m-1):
   if y not in(a[i][j],a[i+1][j],a[i][j+1]):
    k,l=i,j
    while k<n-1 and a[k+1][l]-y:k+=1
    while l<m-1 and a[k][l+1]-y:l+=1
    p+=[[r[j:l+1]for r in a[i:k+1]]]
    for r in a[i:k+1]:r[j:l+1]=[y]*(l-j+1)
 p.sort(key=lambda r:sum(r,[]).count(z)-L(r)*L(r[0]))
 for r in p:
  n,m=L(r),L(r[0])
  for i in R(L(b)-n+1):
   for j in R(L(b[0])-m+1):
    if all(b[i+u][j+v]==(X,c)[c!=z]for u,s in E(r)for v,c in E(s)):
     for k in R(n):b[i+k][j:j+m]=r[k]
 return b
