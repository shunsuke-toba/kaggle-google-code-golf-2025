p=lambda g,r=range(16):max((sum({*i[b:d]}=={v}for i in g[a:c])*(d-b),a-c,[[v*(a<=i<c)*(b<=j<d)for j in r]for i in r])for a in r
for b in r if(v:=g[a][b])for c in r for d in r)[2]