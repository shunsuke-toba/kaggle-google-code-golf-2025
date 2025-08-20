R=range(7)
p=lambda g:max(([x[c:c+3]for x in g[i:i+3]]for i in R for c in R),key=lambda t:(r:=sum(t,[])).count(1)*2+r.count(8))
