import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from math import sqrt

#the parameters that can be changed by user
#the A value that can be changed by user
k=2
V=1
A=1


#ultily functions

#we have a system of first order of ode
#let us define that s=(x,y) 
#    | x |        | dx/dt |
# s= |   | ,ds/dt=|       |
#    | y |        | dy/dt |
def dsdt(t,s):
    #unpack the s into x and y
    x,y=s
    vt_y=V*t-y
    dxdt=(x/sqrt(x**2+vt_y**2))*-k*V
    dydt=(vt_y/sqrt(x**2+vt_y**2))*k*V

    #return the differentiation of the column vector
    return [dxdt,dydt]





#init conditions
y0=0
x0=A

#there are a two types of solver given in the vid
# odeint (without init cond)
# solve_ivp(with inti cond)


#the solving
t = np.linspace(0,1,100)#solve for 100 points


solution_s=solve_ivp(dsdt,t_span=(0,max(t)),y0=(x0,y0),t_eval=t)



#comparision for the moving human
def dhumandt(t,human_pos):
    return V
solution_human=solve_ivp(dhumandt,t_span=(0,max(t)),y0=[0],t_eval=t)

#extract the v values
#the T is the transpose 
x_arr=solution_s.y[0]
y_arr=solution_s.y[1]
human_arr=solution_human.y[0]

#plot the graph to t
# plt.plot(x_arr,t,'--')
# plt.plot(y_arr,t)
# plt.plot(human_arr,t)

# plt.ylabel('$x or y$',fontsize=22)
# plt.xlabel("$t$",fontsize=22)

# plt.show()

plt.plot(x_arr,y_arr)
plt.plot(len(human_arr)*[0],human_arr)

plt.ylabel('$y$',fontsize=22)
plt.xlabel("$x$",fontsize=22)

plt.show()