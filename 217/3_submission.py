from numpy import*
p=lambda g:(a:=array(g).reshape(3,3,3,3).swapaxes(1,2),b:=a[a.any((2,3))][0],kron(b>0,b).tolist())[-1]
