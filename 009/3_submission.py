p=lambda g,E=enumerate:[[c[0]or sum(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]})for j,c in E(zip(r,*g))]for i,r in E(g)]
