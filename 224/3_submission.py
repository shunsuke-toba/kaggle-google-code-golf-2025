def p(g):import numpy as t;a=t.array(g);r,c=t.where(a==5);b=a[min(r)+1:max(r),min(c)+1:max(c)];b[[0,-1]]=b[:,[0,-1]]=a[a!=5].max();return a.tolist()
