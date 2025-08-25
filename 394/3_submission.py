def p(g):n=len(g);a=sum(g,[]).index(0);w=g[r:=a//n].count(0);t=n//7+2;return[g[i+(i<t)*2*t-t][a%n:][:w]for i in range(r,r+w)]
