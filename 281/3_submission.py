def p(j):
 R=range;x=w=len(j[0]);u=len(j);v=y=b=c=0
 for i in R(u*w):
  k=i%w;i//=w
  if(q:=j[i][k]):u=min(u,i);v=max(v,i);x=min(x,k);y=max(y,k);q%8and(b<1 and(b:=q)or(q-b and(c:=q)))
 for i in R(u,v+1):
  for k in R(x,y+1):j[i][k]=[b,c][u<i<v and x<k<y]
 return j
