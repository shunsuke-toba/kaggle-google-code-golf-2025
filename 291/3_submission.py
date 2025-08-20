p=lambda g:[[sum(b*(b==c>0==d)for r,s in zip(g,g[1:])for b,c,d in zip(r[1:],s,s[1:]))]]
