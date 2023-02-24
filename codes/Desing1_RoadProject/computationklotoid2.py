from math import *

A=float(input("A:"))
R=float(input("R:"))
L=float(input("L:"))
delta=float(input("Delta:"))

X=round(L-L**5/40/A**4-L**9/3456/A**8,2)
Y=round(L**3/6/A**2-L**7/336/A**6+L**11/42240/A**10,2)
Ro=200/pi
To=round(L/2/R*Ro,4)
Xm=round(X-R*sin(To/Ro),2)
Ym=round(Y+R*cos(To/Ro),2)
Tk=round(Y/sin(To/Ro),2)
Tu=round(X-Y/tan(To/Ro),2)
DR=round(Ym-R,2)
S=round((X**2+Y**2)**0.5,2)
sigma=round(atan(Y/X),4)
alfa=round(delta-2*To,4)
D=round(R*alfa/Ro,2)
t=round((R+DR)*tan(delta/Ro/2),2)
T=round(Xm+t,2)

print("X:{}, Y:{}".format(X,Y))
print("To:",round(To,4))
print("Xm:",Xm)
print("Ym:",Ym)
print("Tk:",Tk)
print("Tu:",Tu)
print("DeltaR:",DR)
print("S:",S)
print("Sigma:",sigma)
print("Alfa:",alfa)
print("D:",D)
print("t:",t)
print("T:",T)