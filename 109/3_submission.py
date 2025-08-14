def p(g):
 v=next(i for i in range(1,len(g[0])-1)if len({r[i]for r in g})<2);H=next(i for i in range(1,len(g)-1)if len({*g[i]})<2);P=[r[:v]for r in g[:H]];M=max(map(max,P));P=[[g[0][v]*(e==M)or e for e in r]for r in P];A=[r+r[::-1]for r in P];return A+A[::-1]
