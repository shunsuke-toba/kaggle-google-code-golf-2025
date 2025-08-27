def p(g):r=range(16);return max((all({*i[b:d]}=={v}for i in g[a:c])*(c-a)*(d-b),[[v*(a<=i<c)*(b<=j<d)for j in r]for i in r])for a in r for b in r if(v:=g[a][b])for c in r[a+1:]for d in r[b+1:])[1]
