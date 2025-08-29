def p(g):
 R=str.replace;a,b={*sum(g,[])}-{0,8}
 for _ in[0]*256:g=[[*map(int,R(R(str(r)[1::3],f'0{b}',f'{a}{b}')[::-1],f'0{a}',f'{b}{a}'))]for r in zip(*g)]
 return g