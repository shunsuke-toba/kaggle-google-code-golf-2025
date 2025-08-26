p=lambda g,E=enumerate:[[c[i]or sum(({*r[:j]}&{*r[j:]}|{*c[:i]}&{*c[i:]})-{r[2]})for j,c in E(zip(*g))]for i,r in E(g)]
