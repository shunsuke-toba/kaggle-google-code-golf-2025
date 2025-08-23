def p(g):
 s=sum(g,[]);A,B=sorted(((i:=s.index(k))//10,(j:=99-s[::-1].index(k))//10,i%10,j%10)for k in{*s}-{0})
 if A[1]<B[0]:x,y=A[1]+1,B[0];c=max(A[2],B[2])+1;d=min(A[3],B[3])
 else:x,y=max(A[0],B[0])+1,min(A[1],B[1]);c=min(A[3],B[3])+1;d=max(A[2],B[2])
 for r in g[x:y]:r[c:d]=[8]*(d-c)
 return g
