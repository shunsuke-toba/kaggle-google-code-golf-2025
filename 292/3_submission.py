def p(g):
 for a in g:a[::3]=[a*3//2for a in a[::3]]
 return g