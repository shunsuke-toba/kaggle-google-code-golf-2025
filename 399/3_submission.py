def p(g):
 r=[[0]*3,[0]*3,[0]*3]
 for i in range(sum(sum(g,[]))//8):r[i*2//3][-i%3]=1
 return r
