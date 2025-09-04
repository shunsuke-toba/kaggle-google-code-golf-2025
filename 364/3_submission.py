def p(g,i=96):
 while i:*g,=zip(*[[(c>0)*(u|c|l|(u>0<l)*2**(i%4)*4)for u,c,l in zip(a,b,[0,*b])]for a,b in zip([30*[0]]+g,g)][::-1]);i-=1
 return[[c.bit_count()*5%14%9for c in r]for r in g]