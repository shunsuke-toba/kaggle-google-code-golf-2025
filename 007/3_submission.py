def p(g,r=range(7)):d={(i+j)%3:c for i in r for j in r if(c:=g[i][j])};return[[d[(i+j)%3]for j in r]for i in r]
