def p(g):
 exec("while max(g[0])<2:g[:]=g[1:]\ng[:]=zip(*g[::-1])\n"*4)
 return[[c*(c>1)for c in r]for r in g]
