def p(g):
 n=len(g);(a,c),*_,(b,d)=[(i,j)for i in range(n)for j in range(n)if g[i][j]]
 if g[a][c+2]:return[*zip(*p([*zip(*g)][::-1])[::-1])]
 return[[4 if i<b and (c+s<j<d-s or s*(j-i==c+2-a or j+i==d+a-2)) else g[i][j]for s in [i<=a]for j in range(n)]for i in range(n)]