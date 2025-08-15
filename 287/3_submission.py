p=lambda g:[[v if v-4 else g[~i%len(g)][~j%len(r)]for j,v in enumerate(r)]for i,r in enumerate(g)]
