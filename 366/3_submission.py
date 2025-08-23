def p(g,E=enumerate,R=range,L=len,F=filter):
 s=sum(g,[]);Z,Y,X=sorted({*s},key=s.count)[-3:]
 T=lambda q:[*map(list,zip(*F(q,zip(*F(q,g)))))]
 a=T(lambda r:Y in r);b=T(lambda r:X in r)
 n,m,p=L(a),L(a[0]),[]
 for i in R(n-1):
  for j in R(m-1):
   if Y not in(a[i][j],a[i+1][j],a[i][j+1]):
    k,l=i,j
    while k<n-1 and a[k+1][l]-Y:k+=1
    while l<m-1 and a[k][l+1]-Y:l+=1
    p+=[[r[j:l+1]for r in a[i:k+1]]]
    for r in a[i:k+1]:r[j:l+1]=[Y]*(l-j+1)
 p.sort(key=lambda r:sum(r,[]).count(Z)-L(r)*L(r[0]))
 for r in p:
  n,m=L(r),L(r[0])
  for i in R(L(b)-n+1):
   for j in R(L(b[0])-m+1):
    if all(b[i+x][j+y]==(X,c)[c!=Z] for x,s in E(r)for y,c in E(s)):
     for k in R(n):b[i+k][j:j+m]=r[k]
 return b
