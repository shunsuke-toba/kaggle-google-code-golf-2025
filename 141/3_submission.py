def p(g):a=sum(g,[]);b=a.index(v:=max(a));a=range(n:=len(g));return[[v*(j in{i+b%n-b//n,b//n+b%n-i})for j in a]for i in a]
