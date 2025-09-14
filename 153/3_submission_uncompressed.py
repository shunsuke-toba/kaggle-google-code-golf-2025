
def p(g):
 s=sum(g,[]);a,b={*s}-{0}
 f=lambda t:{(x-a,y-b)for a,b in[map(min,*t)]for x,y in t}
 A=f({divmod(i,10)for i in range(100)if s[i]==a})
 B=f({divmod(i,10)for i in range(100)if s[i]==b})
 C={(i,j)for i in range(3)for j in range(3)}
 if f(C-A)-B:A=C-B
 return[[[b,a][(i,j)in A]for j in range(3)]for i in range(3)]
