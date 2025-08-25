def p(g,A=range(-2,3),c=enumerate):k=eval(str(g));[k[i+d].__setitem__(f-~x,b[x+e])for i,b in c(g)for x,a in c(b[:-2])if a*b[x+2]for d in A for f in A if(e:=d*d==f*f)or d*f==0];return k
