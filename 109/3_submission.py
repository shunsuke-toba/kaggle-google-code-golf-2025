p=lambda g:(n:=len(g)//2)and[[e and g[n][0]for e in r[:n]+r[n-1::-1]]for r in g[:n]+g[n-1::-1]]
