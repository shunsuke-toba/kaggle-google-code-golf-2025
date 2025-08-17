from numpy import*;p=lambda g:(g:=array(g),t:=where(g==8),s:=g[t[0].min():t[0].max()+1,t[1].min():t[1].max()+1],putmask(s,s<1,2),g.tolist())[-1]
