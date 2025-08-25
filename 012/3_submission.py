def p(g,A=range(-2,3),c=enumerate):k=eval(str(g));[k[i+d].__setitem__(f-~x,[b[x],h][e])for i,b in c(g)for x,h in c(b[1:-1])if b[x]*b[x+2]for d in A for f in A if(e:=d*d==f*f)or d*f==0];return k
