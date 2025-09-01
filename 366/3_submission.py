def p(g,E=enumerate,R=range,L=len,F=filter,S=sorted):
 s=sum(g,[]);*_,z,y,x=S({*s},key=s.count);a,b=[[*map(list,zip(*F(t:=lambda r:c in r,zip(*F(t,g)))))]for c in(y,x)];n,m,p=L(a),L(a[0]),[]
 for o in R(n*m):
  if a[k:=(i:=o//m)][j:=o%m]^y:
   while a[k+1-n][l:=j]^y:k+=1
   while l+1<m and a[k][l+1]^y:l+=1
   q=a[i:k+1];t=[r[j:l+1]for r in q];p+=(-L(s:=sum(t,[]))+s.count(z),t),
   for r in q:r[j:l+1]=[y]*(l-j+1)
 for _,r in S(p):
  for i in R(L(b)-L(r)+1):
   for j in R(L(b[0])-L(r[0])+1):
    if all(b[i+u][j+v]==(x,c)[c!=z]for u,s in E(r)for v,c in E(s)):
     for k,s in E(r):b[i+k][j:j+L(s)]=s
 return b