def p(g,r=range(10)):
 M,*_,m=sorted(j-i for i in r for j in r if(v:=g[i][j])==5 or v%5 and(c:=v,d:=j-i)and 0);return[[c*(j-i in[d]+[m+2]*(m>d)+[M-2]*(M<d))for j in r]for i in r]