def p(g):
 s=sum(g,[]);a,b={*s}-{0};f=lambda s:{(x-a,y-b)for a,b in[map(min,*s)]for x,y in s};A,B=[f({divmod(i,10)for i in range(100)if s[i]==c})for c in(a,b)];r=range(3);c={(i,j)for i in r for j in r}
 if f(c-A)-B:A=c-B
 return[[[b,a][(i,j)in A]for j in r]for i in r]