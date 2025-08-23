def p(g,R=range):
 n=len(g);v=max(sum(g,[]))
 D=lambda r,c,t,m,b=0:[[v if(d:=max(abs(2*i-2*r-t+1),abs(2*j-2*c-t+1)))and d%(t*2+2)==-~t and d<(m+m+1)*-~t else b for j in R(n)]for i in R(n)]
 return next(D(r,c,t,n,5)for k in R(n)for r,c in((k,0),(0,k))for t in(1,2)for m in(2,3)if D(r,c,t,m)==g)
