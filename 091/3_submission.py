from numpy import*
def p(g):g=array(g);a,b=where(g==5);return g[max(a.min()-1,0):a.max()+2,b.min():b.max()+1].tolist()
