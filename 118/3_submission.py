def p(g):
 h=len(g);w=len(g[0]);R=range;u=[];f=lambda y,x:((a:=g[y][x])==2)-2*(a<1 or(y,x)in u);t=2
 while 1:
  B,_,I,J,t=max((sum(f(a,j)for a in R(i-r,i+r+1)if-1<a<h)+sum(f(i,c)for c in R(j-r,j+r+1)if-1<c<w)-f(i,j),-r,i,j,r)for r in(3,2)[:4-t]for i in R(h)for j in R(w))
  if B<1:return g
  for d in R(-t,t+1):
   for y,x in(I+d,J),(I,J+d):u+=(y,x),;g[y][x]+=3*(g[y][x]==5)