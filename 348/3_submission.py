def p(g,E=enumerate):c=g[0].index(7);return[[(v,7+(j-c)%2)[abs(j-c)<sum(map(sum,g))//7-i]for j,v in E(r)]for i,r in E(g)]
