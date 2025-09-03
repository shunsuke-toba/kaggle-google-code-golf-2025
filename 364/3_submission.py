def p(g):
 for _ in g:z=[[0]*30];g=[[c and(a|b|d|e|((v:=a+b+d+e&3)<2)*4|(v>2)*8*((b+d>0)+(a+e>0)*2))for a,b,c,d,e in zip(s,[0]+t,t,t[1:]+[0],u)]for s,t,u in zip(z+g,g,g[1:]+z)]
 return[[c%8%6*2+c//27*-5for c in r]for r in g]