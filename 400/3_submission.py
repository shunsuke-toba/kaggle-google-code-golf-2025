p=lambda g:(a:=sum(g,[]).index(1))and[[min({g[i][~j],g[~i][j],g[~i][~j]}-{1})for j in range(a%24,a%24+5)]for i in range(a//24,a//24+5)]
