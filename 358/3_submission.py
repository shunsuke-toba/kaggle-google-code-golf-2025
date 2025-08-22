def p(g,R=range,L=len,F=filter):
 r=c=0
 while L({*g[r]})<3:r+=1
 a=g[r];s=[*F(None,a)];d=a.index(s[0]);n=L(s)
 for j in R(L(a)):a[j]=s[(j-d)%n]
 C=*zip(*g),
 while L({*C[c]})<3:c+=1
 s=[*F(None,C[c])];d=C[c].index(s[0])
 for i in R(L(g)):g[i][c]=s[(i-d)%n]
 return g