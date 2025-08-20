def p(g,E=enumerate,R=range,L=len,F=filter):
 C=sorted({*(s:=sum(g,[]))},key=s.count)
 X,Y,Z=C[-1],C[-2],C[-3]
 T=lambda q:[*map(list,zip(*F(q,zip(*F(q,g)))))]
 a=T(lambda r:r.count(Y));b=T(lambda r:r.count(X))
 n,m,p=L(a),L(a[0]),[]
 for i in R(n-1):
  for j in R(m-1):
    if Y!=a[i][j]!=Y!=a[i+1][j]!=Y!=a[i][j+1]:
     k,l=i,j
     while k+1<n and a[k+1][l]!=Y:k+=1
     while l+1<m and a[k][l+1]!=Y:l+=1
     p+=[[a[x][j:l+1]for x in R(i,k+1)]]
     for x in R(i,k+1):a[x][j:l+1]=[Y]*(l-j+1)
 p.sort(key=lambda r:sum(r,[]).count(Z)-L(r)*L(r[0]))
 N,M=L(b),L(b[0])
 for r in p:
  n,m=L(r),L(r[0])
  for i in R(N-n+1):
   for j in R(M-m+1):
    if all(c==Z and b[i+x][j+y]==X or b[i+x][j+y]==c!=Z for x,s in E(r)for y,c in E(s)):
     for k in R(n):b[i+k][j:j+m]=r[k]
 return b