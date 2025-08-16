from numpy import*
def p(g):g=array(g);a,b=where(g);return g[a.min():a.max()+1,b.min():b.max()+1].tolist()
