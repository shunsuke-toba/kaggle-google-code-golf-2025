def p(g):
 s=10;R=range(s);f=sum(g,[]);k=sum({*f})-2;i=f.index(2);a=(i//s,i%s)[b:=k in g[i//s]]+(k>f[i-s+9*b]);return[[(3,k)[g[r][c]|g[(2*a+~r,r)[b]%s][(c,2*a+~c)[b]%s]>0]for c in R]for r in R]