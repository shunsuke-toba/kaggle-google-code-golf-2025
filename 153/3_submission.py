def p(g):
 s=sum(g,[]);a,b={*s}-{0};f=lambda S:{(x-a,y-b)for a,b in[map(min,*S)]for x,y in S};A,B=[f({divmod(i,10)for i in range(100)if s[i]==c})for c in(a,b)];R=0,1,2
 if f({(i,j)for i in R for j in R}-A)^B:a,b,A=b,a,B
 return[[[b,a][(i,j)in A]for j in R]for i in R]