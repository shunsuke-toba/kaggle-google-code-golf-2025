def p(m):
 t=sum(m,[]);v=min({*t}-{0},key=t.count);f=lambda A:[i for i,a in enumerate(A)if v in a];A=m[(L:=f(m))[0]:L[-1]+1]
 return[r[(C:=f(zip(*A)))[0]:C[-1]+1]for r in A]