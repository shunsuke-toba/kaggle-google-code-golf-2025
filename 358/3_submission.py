def p(g,R=range):
 r=0
 while len({*g[r]})<3:r+=1
 a=g[r]
 s=[*filter(None,a)];d=a.index(s[0])
 for j in R(len(a)):a[j]=s[(j-d)%len(s)]
 C=(*zip(*g),);c=0
 while len({*C[c]})<3:c+=1
 s=[*filter(None,C[c])];d=C[c].index(s[0])
 for i in R(len(g)):g[i][c]=s[(i-d)%len(s)]
 return g
