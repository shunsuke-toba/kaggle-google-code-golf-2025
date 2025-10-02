def p(g):
 t=sum(g,[]);s=[i for i in range(30)if(i%10<3)*t[i]];n=1
 while{v:=t[n+i]for i in s}-{v+len(s)%t.count(v)}:n+=1
 for k in s:k+=n;g[k//10][k%10]=5
 return g