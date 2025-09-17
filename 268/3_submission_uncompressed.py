def p(g):
 n=len(g);(a,c),*_,(b,d)=[(i//n,i%n)for i in range(n*n)if g[i//n][i%n]]
 if g[a][c+2]:return[*zip(*p([*zip(*g)][::-1])[::-1])]
 return[[4 if i<b and (c+(s:=i<=a)<j<d-s or s*(j-i==c+2-a or j+i==d+a-2)) else g[i][j]for j in range(n)]for i in range(n)]