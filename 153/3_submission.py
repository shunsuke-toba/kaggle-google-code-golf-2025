def p(g):
 P={}
 for i in range(10):
  for j in range(10):
   if g[i][j]:P[g[i][j]]=P.get(g[i][j],[])+[(i,j)]
 C=list(P)
 def n(s):r,c=zip(*s);m,M,n,N=min(r),max(r),min(c),max(c);return[(R-m,C-n)for R,C in s],M-m+1,N-n+1
 p1,h1,w1=n(P[C[0]]);p2,h2,w2=n(P[C[1]]);B=F=0
 for r1 in range(4-h1):
  for c1 in range(4-w1):
   for r2 in range(4-h2):
    for c2 in range(4-w2):
     T=[[0]*3for _ in range(3)]
     for r,c in p1:
      if-1<r+r1<3>c+c1>-1:T[r+r1][c+c1]=C[0]
     for r,c in p2:
      if-1<r+r2<3>c+c2>-1and not T[r+r2][c+c2]:T[r+r2][c+c2]=C[1]
     f=sum(x>0for R in T for x in R)
     if f>F:F,B=f,[R[:]for R in T]
 return B or[[0]*3for _ in range(3)]
