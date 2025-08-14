def p(g):
 r=range(10);s={*sum(g,[])}-{0};f=lambda c:(x:=[i for i in r if c in g[i]],y:=[j for j in r if c in[r[j]for r in g]],[r[y[0]:y[-1]+1]for r in g[x[0]:x[-1]+1]])[2];a=b=0
 for c in s:m=f(c);d=len(sum(m,[]));m==[r[::-1]for r in m]and d>a and(a:=d,b:=m)
 return b or f(sorted(s)[len(s)//2])
