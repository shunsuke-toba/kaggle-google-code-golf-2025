def p(g):

 s=sum(g,[]);a,b={*s}-{0};f=lambda s:{(x-a,y-b)for a,b in[map(min,*s)]for x,y in s};A,B=[f({divmod(i,10)for i in range(100)if s[i]==c})for c in(a,b)];c={(i,j)for i in range(3)for j in range(3)}
 if f(c-A)-B:A=c-B
 return[[[b,a][(i,j)in A]for j in range(3)]for i in range(3)]