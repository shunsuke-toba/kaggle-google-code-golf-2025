def p(j,A=range(-2,3),c=enumerate):k=[*map(list,j)];[k[i+d].__setitem__(x+f,[b[x-1],h][e])for i,b in c(j)for x,h in c(b)if h!=0<b[x-1]*b[x+1]for d in A for f in A if(e:=d*d==f*f)or d*f==0];return k
