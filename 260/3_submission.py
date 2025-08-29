def p(g,r=range(10)):
 a=[];[v%5 and(c:=v,d:=j-i)or a.append(j-i) for i in r for j in r if(v:=g[i][j])];M,*_,m=sorted(a);return[[c*(j-i in[d]+[m+2]*(m>d)+[M-2]*(M<d))for j in r]for i in r]