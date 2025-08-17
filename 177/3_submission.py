from numpy import*
p=lambda g:(g:=array(g),w:=where(g),g[min(w[0]):-~max(w[0]),min(w[1]):-~max(w[1])][:,::-1].tolist())[2]
