def p(g):
 f=sum(g,[]);c=min(set(f),key=f.count);r={};L=len;w=g[0]
 for k in range(9*L(g)*L(w)):
  i,j=k//L(w)%L(g),k%L(w)
  if g[i][j]==c:
   n=[g[i+a][j+b]for a,b in[(-1,0),(1,0),(0,-1),(0,1)]if-1<i+a<L(g)>-1<j+b<L(w)and g[i+a][j+b]!=c]
   if n and n.count(s:=max(set(n),key=n.count))>1:g[i][j]=s;r[s]=r.get(s,0)+1
 return[[max(r,key=r.get)if r else c]]