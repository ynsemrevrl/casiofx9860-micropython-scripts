from math import *

R=float(input("R:"))
Vp=float(input("Vp:"))
delta=float(input("Delta:"))
L=round(Vp**3/(18.7*R),2)
print("L(ilk):",L)
A=round((L*R)**0.5,3)
print("A(ilk):",A)
A=round(A,0)
kalan=A%10
A=round(A+10-kalan,0)
print("A(ustte yuvarlanmıs):",A)
L=round(A**2/R,2)
print("L(yeni):",L)

X=round(L-L**5/40/A**4-L**9/3456/A**8,3)
Y=round(L**3/6/A**2-L**7/336/A**6+L**11/42240/A**10,3)
Ro=200/pi
To=round(L/2/R*Ro,4)
Xm=round(X-R*sin(To/Ro),3)
Ym=round(Y+R*cos(To/Ro),3)
Tk=round(Y/sin(To/Ro),3)
Tu=round(X-Y/tan(To/Ro),3)
DR=round(Ym-R,2)
S=round((X**2+Y**2)**0.5,3)
sigma=round(atan(Y/X),4)
alfa=round(delta-2*To,4)
D=round(R*alfa/Ro,3)
t=round((R+DR)*tan(delta/Ro/2),3)
T=round(Xm+t,3)

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
