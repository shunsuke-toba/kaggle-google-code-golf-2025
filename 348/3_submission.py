def p(g,E=enumerate):c=g[0].index(7);return[[(7+(j-c)%2)*(abs(j-c)<g.index(g[-1])-i)for j,_ in E(r)]for i,r in E(g)]
