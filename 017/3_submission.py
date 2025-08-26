p=lambda g,s=1,d={},r=range(21):any((v:=g[i][j])and d.setdefault((i%s,j%s),v)-v for j in r for i in r)and p(g,s+1,{})or[[d[i%s,j%s]for j in r]for i in r]
