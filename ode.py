import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
from math import sqrt
from matplotlib.animation import PillowWriter

#getting inputs from user
A_input=input("what values of A:(ex:1,3,5)").split(',')
A_input=[int(x) for x in A_input]
print(A_input)
k_input=input("v value:(ex:1,2,3)").split(',')
k_input=[int(x) for x in k_input]


#resolution
V=1
t = np.linspace(0,6,10)#solve for 100 points between 0 to 1


#ultility functions
#we have a system of first order of ode
#let us define that s=(x,y) 
#    | x |        | dx/dt |
# s= |   | ,ds/dt=|       |
#    | y |        | dy/dt |
def solve_and_plot_single(chosen_A,k):
    #inner function
    def dsdt(t,s):
        #unpack the s into x and y
        x,y=s
        vt_y=V*t-y
        dxdt=(x/sqrt(x**2+vt_y**2))*-k*V
        dydt=(vt_y/sqrt(x**2+vt_y**2))*k*V

        #return the differentiation of the column vector
        return [dxdt,dydt]

    # picking init conditions
    y0=0
    x0=chosen_A

    #there are a two types of solver given in the vid
    # odeint (old solving function:not recommended)
    # solve_ivp(with inti cond)
    solution_s=solve_ivp(dsdt,t_span=(0,max(t)),y0=(x0,y0),t_eval=t)

    #extract the x and y values
    #the T is the transpose 
    x_arr=solution_s.y[0]
    y_arr=solution_s.y[1]


    #plot the graph to t(not used for observing position to time relationship)
    # plt.plot(x_arr,t,'--')
    # plt.plot(y_arr,t)
    # plt.plot(human_arr,t)
    # plt.ylabel('$x or y$',fontsize=22)
    # plt.xlabel("$t$",fontsize=22)
    # plt.show()
    plt.plot(x_arr,y_arr,label=f"A={chosen_A} k={k}")
    


#comparision for the moving human
#human always go with 1V
def dhumandt(t,human_pos):
    return V
solution_human=solve_ivp(dhumandt,t_span=(0,max(t)),y0=[0],t_eval=t)
human_arr=solution_human.y[0]
plt.plot(len(human_arr)*[0],human_arr)

#plot the dog
#different A
for a_val in A_input:
    for k_val in k_input:
        solve_and_plot_single(a_val,k_val)




#setting the label for axes
plt.ylabel('y',fontsize=22)
plt.xlabel("x",fontsize=22)

#show the plot
plt.legend()
plt.show()

