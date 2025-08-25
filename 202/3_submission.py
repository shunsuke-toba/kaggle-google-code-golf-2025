p=lambda g,z=zip:len({0,*g[0]})>2and[*z(*p([*z(*g)]))]or[[v*all(max(s)-max(r)or s[i]for s in g)for i,v in enumerate(r)]for r in g]
