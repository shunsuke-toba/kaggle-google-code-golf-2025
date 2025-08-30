def p(g,r=range(10)):
 a,*_,b=sorted([j-i,(c:=v,d:=j-i)[1]][v%5>0]for i in r for j in r if(v:=g[i][j]));return[[c*(j-i in(d,b+2*(b>d),a-2*(a<d)))for j in r]for i in r]