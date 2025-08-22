p=lambda g:(g:=sum(g,[]),n:=g.count(0),r:=range(3*n))and[[g[i%3*3+j%3]*(i//3*n+j//3<9-n)for j in r]for i in r]
