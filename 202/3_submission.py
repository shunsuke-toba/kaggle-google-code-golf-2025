p=lambda g,z=zip:len({0,*g[0]})>2 and[*z(*p([*z(*g)]))]or[[0if any(max(s)==max(r)>s[i]for s in g)else v for i,v in enumerate(r)]for r in g]

