def p(g,A=range(-2,3),c=enumerate):k=eval(str(g));[k[i+d].__setitem__(x+f,[b[x-1],h][e])for i,b in c(g)for x,h in c(b)if h and b[x-1]*b[x+1]for d in A for f in A if(e:=d*d==f*f)or d*f==0];return k
