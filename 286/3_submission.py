def p(g):
 a,b=map(str,{*sum(g,[])}-{0,8})
 for _ in[0]*160:g=[[*map(int,str(R)[1::3].replace('0'+b,a+b)[::-1].replace('0'+a,b+a))]for R in zip(*g)]
 return g