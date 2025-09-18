def p(g):
 k=max(r[i-1]&r[i]&r[i+1]&p[i]for r,p in zip(g[1:],g)for i in range(19))
 return[*zip(*[(y:=bytes(c).rfind(k)+1)and c[:y]+(max(c[y:]),)*(20-y) or c for c in zip(*g)])]