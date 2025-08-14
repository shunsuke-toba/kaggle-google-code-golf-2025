def p(a):
 h=len(a);w=len(a[0]);R=range
 for y in R(h-6):
  for x in R(w-6):
   if all((a[y+i][x+j]==5)==(i*j*(i-6)*(j-6)<1)for i in R(7)for j in R(7)):
    q=[(i,j)for i in R(5)for j in R(5)if (v:=a[y+1+i][x+1+j])>1 and (c:=v)]
    u,v=zip(*q);Y,X=min(u),min(v)
    S={(i-Y,j-X)for i,j in q};H,W=max(u)-Y+1,max(v)-X+1
    for Y in R(h-H+1):
     for X in R(w-W+1):
      if all(((i,j)in S)==(a[Y+i][X+j]==1)for i in R(H)for j in R(W))and all(a[Y+i][X+j]^1 for i in R(-1,H+1)for j in R(-1,W+1)if not(0<=i<H and 0<=j<W)and 0<=Y+i<h and 0<=X+j<w):
       for i,j in S:a[Y+i][X+j]=c
    return a
