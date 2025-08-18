import numpy as n
def p(g):g=n.array(g);y,x=n.where(z:=g>1);return (g*z)[y.min():y.max()+1,x.min():x.max()+1].tolist()
