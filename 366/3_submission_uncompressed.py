def p(g):
 s=sum(g,[]);*_,z,y,x=sorted({*s},key=s.count);a,b=[[*map(list,zip(*filter(t:=lambda r:c in r,zip(*filter(t,g)))))]for c in(y,x)];n,m,p=len(a),len(a[0]),[]
 for o in range(n*m):
  if a[k:=(i:=o//m)][j:=o%m]^y:
   while a[k+1-n][l:=j]^y:k+=1
   while (a[k]+[y])[l]^y:l+=1
   q=a[i:k+1];p+=(-len(s:=sum(t:=[r[j:l]for r in q],[]))+s.count(z),t),
   for r in q:r[j:l]=[y]*(l-j)
 for _,r in sorted(p):
  for i in range(n-len(r)+1):
   for j in range(m-len(r[0])+1):
    if all(b[i+u][j+v]==(x,c)[c!=z]for u,s in enumerate(r)for v,c in enumerate(s)):
     for k,s in enumerate(r):b[i+k][j:j+len(s)]=s
 return b