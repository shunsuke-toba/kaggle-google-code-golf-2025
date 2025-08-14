def p(g,Z=range):
 R=len(g);C=len(g[0]);A=Z(R);z=[c for c in Z(C)if all(g[r][c]==0for r in A)];s=[];t=0
 for e in z+[C]:
  if t<e:s.append([g[r][t:e]for r in A]);t=e+1
 if not s:return[[0]*C for _ in A]
 f=lambda x:[(r,c)for r in Z(len(x))for c in Z(len(x[0]))if x[r][c]==5]
 r=[s[0]]
 for i in Z(1,len(s)):
  c=[x[:]for x in s[i]];p=f(r[-1]);q=f(c);p=next((a for a,b in p if b==len(r[-1][0])-1),None);l=next((a for a,b in q if b==0),None)
  if p is not None and l is not None:
   h=p-l
   if h:n=[[0]*len(c[0])for _ in A];[n.__setitem__(r+h,c[r][:])for r in A if 0<=r+h<R];c=n
  r.append(c)
 o=[[]for _ in A]
 for x in r:
  for i in A:o[i].extend(x[i])
 n=[row[:]for row in o]
 for j in A:
  for k in Z(len(o[0])):
   if o[j][k]==5:
    b=[o[j+d][k+e]for d,e in[(-1,0),(1,0),(0,-1),(0,1)]if 0<=j+d<R and 0<=k+e<len(o[0])and o[j+d][k+e]not in[0,5]]
    n[j][k]=b[0]if b else 0
 return[[n[j][k]for k in Z(len(n[0]))if any(n[i][k]for i in A)]for j in A]