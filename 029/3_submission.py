def p(g):
 b=bytes(sum(g,[]));w=len(g[0]);k=0
 while{*b[(n:=b.find(k)):(m:=b.rfind(k)):w]}^{k}:k+=1
 return[r[n%w+1:m%w]for r in g[n//w+1:m//w]]