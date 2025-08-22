def p(g,L=len,F=filter):
 r=c=0
 while L({*g[r]})<3:r+=1
 a=g[r];s=[*F(None,a)];n=L(s);d=a.index(s[0])
 a[:]=(s*(L(a)//n+2))[-d%n:][:L(a)]
 C=*zip(*g),
 while L({*C[c]})<3:c+=1
 s=[*F(None,C[c])];d=C[c].index(s[0])
 for i in range(L(g)):g[i][c]=s[(i-d)%n]
 return g