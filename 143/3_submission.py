def p(g):
 t=sum(g,[]);s=[i for i in range(30)if(i%10<3)*t[i]];n=1
 while{v:=t[n+i]for i in s}-{v}or t.count(v)-len(s):n+=1
 for i in s:g[(k:=n+i)//10][k%10]=5
 return g