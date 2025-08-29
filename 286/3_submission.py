import re
def p(g):
 S=re.sub;a,b={*sum(g,[])}-{0,8}
 for _ in[a,b]*256:g=[[*map(int,S(f'0(?={a})',f'{b}',S(f'0(?={b})',f'{a}',str(r)[1::3])[::-1]))]for r in zip(*g)]
 return g