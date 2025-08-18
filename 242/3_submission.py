def p(g):
 for r in g:
  if 0 in r:a=r.index(0);return[g[~g.index(r)-k][~a:~a-3:-1]for k in(0,1,2)]
