def p(g):k=range(len(g));p,q,_=sorted((i,j)for i in k for j in k if g[i][j]);a,b=q;return[[g[a][b]*(max(a-i,i-a,b-j,j-b)%(a-p[0])<1)for j in k]for i in k]
