def p(g):
 a,b=map(str,{*sum(g,[])}-{0,8});R=str.replace
 for _ in[0]*256:g=[[*map(int,R(R(str(r)[1::3],'0'+b,a+b)[::-1],'0'+a,b+a))]for r in zip(*g)]
 return g