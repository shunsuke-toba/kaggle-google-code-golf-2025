def p(g):a=sum(g,[]);y,x=divmod(a.index(v:=max(a)),len(g[0]));return[[[b,v][i-j==y-x or i+j==y+x]for j,b in enumerate(r)]for i,r in enumerate(g)]
