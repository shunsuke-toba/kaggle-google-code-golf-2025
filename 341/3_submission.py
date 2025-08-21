def p(g):
 s=sum(g,[]);A,B=[(i//10,j//10,i%10,j%10)for k in{*s}-{0}for i,j in[(s.index(k),99-s[::-1].index(k))]]
 if A[0]>B[0]:A,B=B,A
 if A[1]<B[0]:
  c=max(A[2],B[2])+1;d=min(A[3],B[3])
  for r in g[A[1]+1:B[0]]:r[c:d]=[8]*(d-c)
 else:
  if A[2]>B[2]:A,B=B,A
  for r in g[max(A[0],B[0])+1:min(A[1],B[1])]:r[A[3]+1:B[2]]=[8]*(B[2]-A[3]-1)
 return g
