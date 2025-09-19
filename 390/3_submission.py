def p(g):
 for _ in g*4:g=[[t,t[:(j:=t[3]<2)]+t[j:][6::-1]+t[j+7:]][{0,5}<{*t}] for t in zip(*g[::-1])]
 return g