def p(g):
 s=sum(g,[]);a,b={*s}-{0};f=lambda s:{(x-a,y-b)for a,b in[map(min,zip(*s))]for x,y in s};A,B=[f({divmod(i,10)for i in range(100)if s[i]==c})for c in(a,b)]
 if f({(i//3,i%3)for i in range(9)}-A)^B:a,b,A=b,a,B
 o=[[b]*3,[b]*3,[b]*3]
 for x,y in A:o[x][y]=a
 return o

