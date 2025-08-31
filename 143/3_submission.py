def p(g):
 t=sum(g,[])
 s=[i+i//3*7 for i in range(9)if t[i+i//3*7]]
 n=1
 while{v:=t[n+i]for i in s}-{v}or t.count(v)-len(s):n+=1
 for i in s:g[(n+i)//10][(n+i)%10]=5
 return g